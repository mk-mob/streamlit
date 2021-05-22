import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamlit 超入門')
st.write('DataFrame')

# df = pd.DataFrame({
#     "1列目":[1,2,3,4],
#     "2列目":[10,20,30,40]
# })

# st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50, 50] + [35.69, 139.70],
#     columns=['lat', 'lon']
# )
# st.map(df)

# if st.checkbox('Show Image'):
#     img = Image.open('tacolice.jpg')
#     st.image(img, caption='タコライス', use_column_width=True)

# option = st.selectbox(
#     'あなたが好きな数字を指定してください',
#     list(range(1,11))
# )

# 'あなたの好きな数字は、', option, 'です'

# text = st.sidebar.text_input('あなたの趣味を教えてください')
# 'あなたの趣味は、', text, 'です'

# cond =st.sidebar.slider('あなたの調子は?', 0, 100, 50)

# 'あなたの調子は、', cond, 'です'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration{i+1}")
    bar.progress(i+1)
    time.sleep(0.1)

lc,rc = st.beta_columns(2)
button = lc.button('右カラムに文字を表示')
if button:
    rc.write('ここは右カラム')

df = pd.DataFrame(
    np.random.rand(20,3)*[20,20,20],
    columns=['x', 'y', 'z']
)
exp = st.beta_expander('棒グラフ表示')

exp.line_chart(df)


