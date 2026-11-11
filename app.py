import os
import re
import time
import random
import streamlit as st

# ---------- 1. PAGE SETUP ----------
st.set_page_config(page_title="For you 💌", page_icon="💌", layout="centered")

# ---------- 2. YOUR DETAILS ----------
HER_NAME = "Babli"
MY_NAME = "Rohan"

# Each line has the text she reads AND the voice file she can play.
# Record each voice note, save as mp3, put it in a folder called "voice".
LINES = [
    {"text": f"Heyy {HER_NAME}. Please read this slowly, one line at a time.", "audio": "voice/line1.mp3"},
    {"text": "What I said yesterday was not what I really meant.", "audio": "voice/line2.mp3"},
    {"text": "But je zhala tyasathi mala guilt hotoy. Majhya kadun jara jasta only zhala.", "audio": "voice/line3.mp3"},
    {"text": "I am sorry my tone made you feel unheard.", "audio": "voice/line4.mp3"},
    {"text": f"{HER_NAME}, possible asel tar mala maaf kar.", "audio": "voice/line5.mp3"},
    {"text": "Next time I will speak slowly.", "audio": "voice/line6.mp3"},
    {"text": f"You matter more to me than winning any argument, {HER_NAME}.", "audio": "voice/line7.mp3"},
]

# The big message. A blank line = a new paragraph. **text** = bold.
BIG_MESSAGE = '''**My Dear Bhumika ❤️**

First of all, I'm really sorry for everything I said to you in anger. मला माहिती आहे की रागाच्या भरात मी तुला खूप काही बोललो, काही गोष्टी अशा बोललो ज्या मला खरंतर बोलायला नको होत्या. And I'm genuinely sorry for hurting you.

But आज मला तुला माझ्या मनात काय होतं ते सांगायचं आहे.

तुला आठवतंय ना Diwali Padwa ला तू मला त्या ring चा photo पाठवला होता आणि तुला ती ring gift म्हणून हवी होती? मी ती गोष्ट seriously घेतली होती. त्याच दिवशी संध्याकाळी मी market मध्ये गेलो आणि तुझ्यासाठी ती ring घेऊन आलो.

पण माझ्या मनात एक वेगळाच विचार होता. मला वाटलं की जेव्हा आपण प्रत्यक्ष भेटू, तेव्हा मी तुला ती ring देईन आणि तुला proper propose करेन. कारण माझ्यासाठी तो moment special होता. मला तो video call वर किंवा घाईघाईत करायचा नव्हता. I wanted to look into your eyes, hold your hand and propose to you in person.

But maybe तू माझ्याकडून वेगळं काहीतरी expect करत होतीस. तुला वाटलं असेल की आपल्यात distance आहे, तर मी video call वर काहीतरी romantic surprise किंवा proposal करायला हवं होतं. And I understand your expectations too. आपले दोघांचे विचार वेगळे होते, पण त्याचा अर्थ असा नाही की मी तुझ्यासाठी काहीच केलं नव्हतं.

आणि तुला एक गोष्ट आठवते का? Last time तू मला तुझा photo दिलास पण तेव्हा मी तुला विचारलं होतं, "Can I give you my photo?" आणि तू म्हणाली होतीस की तुझ्याकडे wallet नाहीये.

ती छोटीशी गोष्टसुद्धा माझ्या लक्षात होती. म्हणून मी तुझ्यासाठी एक wallet सुद्धा घेतलं. मला वाटलं की त्यात माझा photo ठेवशील आणि तो तुझ्यासोबत नेहमी असेल. ❤️

माझ्या मनात एक छोटासा surprise plan होता. आपण संध्याकाळी river side किंवा श्रीवर्धन जायचं, तिथे तुला ती ring द्यायची, तुझ्या हातात ती ring घालायची, तुला proper propose करायचं आणि सोबत wallet सुद्धा द्यायचं. मला फक्त तुझ्या चेहऱ्यावरचं happiness बघायचं होतं.

पण त्याआधीच आपलं भांडण झालं. जेव्हा तू म्हणालीस की मी काहीच करत नाही, surprise plan करत नाही, तेव्हा मला खूप वाईट वाटलं. कारण यावेळी खरंच मी तुझ्यासाठी सगळं plan केलं होतं.

म्हणून रागाच्या भरात मी तुला सगळं दाखवलं आणि त्यानंतर खूप काही बोललो. But honestly, मला माझ्या रागावर control ठेवायला हवा होता. माझा plan खराब झाला म्हणून मी तुला hurt करणं चुकीचं होतं. I'm really sorry for that.

**Bhumika, I was not ignoring your expectations. I just wanted to make that moment more beautiful in my own way.**

मला माहिती आहे की तुलासुद्धा माझ्याकडून surprises आणि efforts अपेक्षित असतात. And I don't want you to feel that I don't care about those things.

**I LOVE YOU, BHUMIKA. ❤️**

I don't want a perfect relationship. I just want us to understand each other's feelings, communicate properly and never let small misunderstandings hurt what we have.

एकच गोष्ट सांगायची आहे, ती ring मी फक्त तुझ्यासाठी घेतली होती. आणि तुला propose करण्याचा माझा विचारसुद्धा तितकाच genuine होता. मला फक्त तो moment तुझ्यासोबत प्रत्यक्ष जगायचा होता.

**I'm sorry for my words, my girl. I love you, and I really wanted to make you feel special. ❤️**

**Yours,**
**Rohan ❤️**'''

# ---------- 3. LOOK + EFFECTS (CSS) ----------
st.markdown(
    """
    <style>
    .stApp { background: linear-gradient(180deg, #fff0f5, #ffe3ec); }
    .card {
        background: white; padding: 18px 20px; border-radius: 14px;
        border-left: 6px solid #e8728f; margin: 14px 0 6px 0;
        font-size: 1.1rem; color: #333; line-height: 1.7;
        animation: fadein 0.8s ease;
    }
    @keyframes fadein { from {opacity:0; transform: translateY(10px);} to {opacity:1; transform:none;} }
    .hearts { position: fixed; top:0; left:0; width:100%; height:100%;
              pointer-events:none; z-index:0; overflow:hidden; }
    .heart { position:absolute; bottom:-60px; opacity:0.7; animation: rise linear infinite; }
    .burst { position:absolute; bottom:-60px; opacity:0.9; animation: rise 4s ease-out forwards; }
    @keyframes rise { to { transform: translateY(-115vh) rotate(25deg); opacity:0; } }
    </style>
    """,
    unsafe_allow_html=True,
)

def floating_hearts():
    rng = random.Random(7)   # fixed seed, so the hearts stay in the same places
    hearts = ""
    for _ in range(14):
        hearts += (
            f'<span class="heart" style="left:{rng.randint(0, 95)}%;'
            f'font-size:{rng.randint(16, 34)}px;'
            f'animation-delay:{rng.uniform(0, 8):.1f}s;'
            f'animation-duration:{rng.uniform(8, 16):.1f}s">'
            f'{rng.choice(["💗", "💖", "🌸", "✨"])}</span>'
        )
    st.markdown(f'<div class="hearts">{hearts}</div>', unsafe_allow_html=True)

def heart_burst():
    rng = random.Random()    # no seed, so every burst looks different
    hearts = ""
    for _ in range(30):
        hearts += (
            f'<span class="burst" style="left:{rng.randint(0, 95)}%;'
            f'font-size:{rng.randint(22, 44)}px;'
            f'animation-delay:{rng.uniform(0, 1.5):.1f}s">'
            f'{rng.choice(["💗", "💖", "💛", "🌸", "✨"])}</span>'
        )
    st.markdown(f'<div class="hearts">{hearts}</div>', unsafe_allow_html=True)

def typewriter(text, placeholder):
    shown = ""
    for ch in text:
        shown += ch
        placeholder.markdown(f'<div class="card">{shown}</div>', unsafe_allow_html=True)
        time.sleep(0.03)

def to_html(paragraph):
    html = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", paragraph)   # **bold** -> <b>bold</b>
    return html.replace("\n", "<br>")                            # new line -> <br>

def show_big_message(animated):
    for paragraph in BIG_MESSAGE.split("\n\n"):
        st.markdown(f'<div class="card">{to_html(paragraph)}</div>', unsafe_allow_html=True)
        if animated:
            time.sleep(1.2)

floating_hearts()

# ---------- 4. MEMORY OF THE APP ----------
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.animate = True
    st.session_state.better = False
    st.session_state.opened = False
    st.session_state.reveal = False

# ---------- 5. TITLE + TABS ----------
st.title("💌 Read it. Then hear it.")
st.caption("Tip: use headphones. The voice is the tone I should have used.")

tab1, tab2, tab3 = st.tabs(["💌 Letter", "💛 Feeling", "🎁 Surprise"])

# ---------- TAB 1: LETTER WITH VOICE ----------
with tab1:
    for i in range(st.session_state.step):
        line = LINES[i]
        is_last = i == st.session_state.step - 1
        if is_last and st.session_state.animate:
            box = st.empty()
            typewriter(line["text"], box)
            st.session_state.animate = False
        else:
            st.markdown(f'<div class="card">{line["text"]}</div>', unsafe_allow_html=True)
        if os.path.exists(line["audio"]):
            st.audio(line["audio"])

    if st.session_state.step < len(LINES):
        if st.button("Next line 💌"):
            st.session_state.step += 1
            st.session_state.animate = True
            st.rerun()
    else:
        st.caption("That was all. Please open the next tab 💛")

# ---------- TAB 2: FEELING ----------
with tab2:
    st.subheader("How are you feeling now?")
    st.write("Take your time. There is no hurry. Press only when you really feel it.")

    pressed = False
    if not st.session_state.better:
        pressed = st.button("I am feeling better 💛")

    if pressed:
        st.session_state.better = True
        st.balloons()
        st.snow()
        heart_burst()
        st.toast("💛")

    if st.session_state.better:
        st.markdown(
            f'<div class="card">Thank you, {HER_NAME}. That makes me really happy. '
            f"Let's talk properly now, and this time my tone will be calm. 💛<br>- {MY_NAME}</div>",
            unsafe_allow_html=True,
        )

# ---------- TAB 3: SURPRISE ----------
with tab3:
    if not st.session_state.opened:
        st.write("When you are ready, open it.")
        if st.button("Open your surprise 🎁"):
            st.session_state.opened = True
            st.session_state.reveal = True
            st.rerun()
    else:
        if st.session_state.reveal:
            heart_burst()
            show_big_message(animated=True)
            st.session_state.reveal = False
            st.balloons()
            st.snow()
        else:
            show_big_message(animated=False)
            