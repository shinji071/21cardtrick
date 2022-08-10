import streamlit as st
question = "何列目にあるか教えてください："
def displayArray(a):
    for i in range(1,8):
        st.write("{0}\t\t{1}\t\t{2}\n".format(a[i-1],a[i+7-1],a[i+14-1]))

st.header('21 Card Trick')
st.write('21 Card Trickと呼ばれる古典カードマジックのオンライン版。指示に従って入力してみてください。')
st.write('列というのは、左から１列目、２列目、３列目と数えます(開発者twitter:@ShinjiEdu)')


a = [i+1 for i in range(21)]
b = [0 for i in range(21)]
c =  [0 for i in range(21)]
displayArray(a);
st.write("数字を一つ覚えてください！")
option = st.selectbox(
     '↑何列目にあなたの数字はありますか？',
     ('-', '1列目', '2列目', '3列目'))

if option == '1列目':
    b[0]=a[7]; b[7]=a[8]; b[14]=a[9];
    b[1]=a[10]; b[8]=a[11]; b[15]=a[12];
    b[2]=a[13]; b[9]=a[0]; b[16]=a[1];
    b[3]=a[2]; b[10]=a[3]; b[17]=a[4];
    b[4]=a[5]; b[11]=a[6]; b[18]=a[14];
    b[5]=a[15]; b[12]=a[16]; b[19]=a[17];
    b[6]=a[18]; b[13]=a[19]; b[20]=a[20];
    displayArray(b);
    option1 = st.selectbox(
     '↑何列目にあなたの数字はありますか？',
     ('-', '1列目', '2列目', '3列目'))
    if option1 == '1列目':
        c[0]=b[7]; c[7]=b[8]; c[14]=b[9];
        c[1]=b[10]; c[8]=b[11]; c[15]=b[12];
        c[2]=b[13]; c[9]=b[0]; c[16]=b[1];
        c[3]=b[2]; c[10]=b[3]; c[17]=b[4];
        c[4]=b[5]; c[11]=b[6]; c[18]=b[14];
        c[5]=b[15]; c[12]=b[16]; c[19]=b[17];
        c[6]=b[18]; c[13]=b[19]; c[20]=b[20];
        displayArray(c);
        option11 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option11 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option11 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option11 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option1 == '2列目':
        c[0]=b[14]; c[7]=b[15]; c[14]=b[16];
        c[1]=b[17]; c[8]=b[18]; c[15]=b[19];
        c[2]=b[20]; c[9]=b[7]; c[16]=b[8];
        c[3]=b[9]; c[10]=b[10]; c[17]=b[11];
        c[4]=b[12]; c[11]=b[13]; c[18]=b[0];
        c[5]=b[1]; c[12]=b[2]; c[19]=b[3];
        c[6]=b[4]; c[13]=b[5]; c[20]=b[6];
        displayArray(c);
        option12 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option12 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option12 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option12 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option1 == '3列目':
        c[0]=b[0]; c[7]=b[1]; c[14]=b[2];
        c[1]=b[3]; c[8]=b[4]; c[15]=b[5];
        c[2]=b[6]; c[9]=b[14]; c[16]=b[15];
        c[3]=b[16]; c[10]=b[17]; c[17]=b[18];
        c[4]=b[19]; c[11]=b[20]; c[18]=b[7];
        c[5]=b[8]; c[12]=b[9]; c[19]=b[10];
        c[6]=b[11]; c[13]=b[12]; c[20]=b[13];
        displayArray(c);
        option13 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option13 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option13 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option13 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))       
elif option == '2列目':
    b[0]=a[14]; b[7]=a[15]; b[14]=a[16];
    b[1]=a[17]; b[8]=a[18]; b[15]=a[19];
    b[2]=a[20]; b[9]=a[7]; b[16]=a[8];
    b[3]=a[9]; b[10]=a[10]; b[17]=a[11];
    b[4]=a[12]; b[11]=a[13]; b[18]=a[0];
    b[5]=a[1]; b[12]=a[2]; b[19]=a[3];
    b[6]=a[4]; b[13]=a[5]; b[20]=a[6];
    displayArray(b);
    option2 = st.selectbox(
     '↑何列目にあなたの数字はありますか？',
     ('-', '1列目', '2列目', '3列目'))
    if option2 == '1列目':
        c[0]=b[7]; c[7]=b[8]; c[14]=b[9];
        c[1]=b[10]; c[8]=b[11]; c[15]=b[12];
        c[2]=b[13]; c[9]=b[0]; c[16]=b[1];
        c[3]=b[2]; c[10]=b[3]; c[17]=b[4];
        c[4]=b[5]; c[11]=b[6]; c[18]=b[14];
        c[5]=b[15]; c[12]=b[16]; c[19]=b[17];
        c[6]=b[18]; c[13]=b[19]; c[20]=b[20];
        displayArray(c);
        option21 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option21 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option21 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option21 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option2 == '2列目':
        c[0]=b[14]; c[7]=b[15]; c[14]=b[16];
        c[1]=b[17]; c[8]=b[18]; c[15]=b[19];
        c[2]=b[20]; c[9]=b[7]; c[16]=b[8];
        c[3]=b[9]; c[10]=b[10]; c[17]=b[11];
        c[4]=b[12]; c[11]=b[13]; c[18]=b[0];
        c[5]=b[1]; c[12]=b[2]; c[19]=b[3];
        c[6]=b[4]; c[13]=b[5]; c[20]=b[6];
        displayArray(c);
        option22 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option22 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option22 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option22 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option2 == '3列目':
        c[0]=b[0]; c[7]=b[1]; c[14]=b[2];
        c[1]=b[3]; c[8]=b[4]; c[15]=b[5];
        c[2]=b[6]; c[9]=b[14]; c[16]=b[15];
        c[3]=b[16]; c[10]=b[17]; c[17]=b[18];
        c[4]=b[19]; c[11]=b[20]; c[18]=b[7];
        c[5]=b[8]; c[12]=b[9]; c[19]=b[10];
        c[6]=b[11]; c[13]=b[12]; c[20]=b[13];
        displayArray(c);
        option23 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option23 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option23 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option23 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
elif option == '3列目':
    b[0]=a[0]; b[7]=a[1]; b[14]=a[2];
    b[1]=a[3]; b[8]=a[4]; b[15]=a[5];
    b[2]=a[6]; b[9]=a[14]; b[16]=a[15];
    b[3]=a[16]; b[10]=a[17]; b[17]=a[18];
    b[4]=a[19]; b[11]=a[20]; b[18]=a[7];
    b[5]=a[8]; b[12]=a[9]; b[19]=a[10];
    b[6]=a[11]; b[13]=a[12]; b[20]=a[13];
    displayArray(b);
    option3 = st.selectbox(
     '↑何列目にあなたの数字はありますか？',
     ('-', '1列目', '2列目', '3列目'))
    if option3 == '1列目':
        c[0]=b[7]; c[7]=b[8]; c[14]=b[9];
        c[1]=b[10]; c[8]=b[11]; c[15]=b[12];
        c[2]=b[13]; c[9]=b[0]; c[16]=b[1];
        c[3]=b[2]; c[10]=b[3]; c[17]=b[4];
        c[4]=b[5]; c[11]=b[6]; c[18]=b[14];
        c[5]=b[15]; c[12]=b[16]; c[19]=b[17];
        c[6]=b[18]; c[13]=b[19]; c[20]=b[20];
        displayArray(c);
        option31 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option31 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option31 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option31 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option3 == '2列目':
        c[0]=b[14]; c[7]=b[15]; c[14]=b[16];
        c[1]=b[17]; c[8]=b[18]; c[15]=b[19];
        c[2]=b[20]; c[9]=b[7]; c[16]=b[8];
        c[3]=b[9]; c[10]=b[10]; c[17]=b[11];
        c[4]=b[12]; c[11]=b[13]; c[18]=b[0];
        c[5]=b[1]; c[12]=b[2]; c[19]=b[3];
        c[6]=b[4]; c[13]=b[5]; c[20]=b[6];
        displayArray(c);
        option32 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option32 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option32 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option32 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
    elif option3 == '3列目':
        c[0]=b[0]; c[7]=b[1]; c[14]=b[2];
        c[1]=b[3]; c[8]=b[4]; c[15]=b[5];
        c[2]=b[6]; c[9]=b[14]; c[16]=b[15];
        c[3]=b[16]; c[10]=b[17]; c[17]=b[18];
        c[4]=b[19]; c[11]=b[20]; c[18]=b[7];
        c[5]=b[8]; c[12]=b[9]; c[19]=b[10];
        c[6]=b[11]; c[13]=b[12]; c[20]=b[13];
        displayArray(c);
        option33 = st.selectbox(
         '↑何列目にあなたの数字はありますか？',
         ('-', '1列目', '2列目', '3列目'))
        if option33 == '1列目':
            st.subheader("あなたの数字は{0}です！".format(c[3]))
        elif option33 == '2列目':
            st.subheader("あなたの数字は{0}です！".format(c[10]))
        elif option33 == '3列目':
            st.subheader("あなたの数字は{0}です！".format(c[17]))
           
