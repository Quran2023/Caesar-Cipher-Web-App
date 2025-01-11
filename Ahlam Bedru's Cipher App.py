

import streamlit as st

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encrypted_text = ''

    for char in message.lower():
        if char == ' ':
            encrypted_text += char
        else:
            index = alphabet.find(char)
            new_index = (index + offset) % len(alphabet)
            encrypted_text += alphabet[new_index]

    return encrypted_text

# Streamlit app layout
st.title("Ahlam Bedru's Cipher App")
st.write(The Caesar cipher is a method of encrypting text by shifting each letter in the message by a number of positions in the alphabet. Try it for yourself!)


# Input for plain text
text = st.text_input("Enter the text to be encrypted:")

# Input for shift value
shift = st.number_input("Enter the shift value (1-25):", min_value=1, max_value=25, value=5)
# Input for shift value

# Button to encrypt
if st.button("Cipher It!"):
    if text:
        encrypted_text = caesar(text, shift)
        st.write('**Plain text:**', text)
        st.write('**Encrypted text:**', encrypted_text)
    else:
        st.warning("Please enter a text to encrypt.")


if st.button("Decipher It!"):
    if text:
        decrypted_text = caesar(text, -shift, decrypt=True) #Use negative shift for decryption
        st.write('**input text:**', text)
        st.write('**Decrypted text:**', decrypted_text)
    else:
        st.warning("Please enter a text to decrypt.")
