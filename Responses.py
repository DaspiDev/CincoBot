from datetime import datetime
import Constants as keys

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message.endswith('cinco'):
        return keys.spanish_response

    if user_message.endswith('c1nc0'):
        return keys.spanish_response

    if user_message.endswith('5'):
        return keys.spanish_response

    if user_message.endswith('sinco'):
        return keys.spanish_response

    if user_message.endswith('five'):
        return keys.english_response

    if user_message.endswith('faiv'):
        return keys.english_response

    if user_message.endswith('fais'):
        return keys.english_response

    if user_message.endswith('faif'):
        return keys.english_response

    if user_message.endswith('101'):
        return "01010000 01101111 01110010 00100000 01100101 01101100 00100000 01100011 01110101 01101100 01101111 00100000 01110100 01100101 00100000 01101100 01100001 00100000 01101000 01101001 01101110 01100011 01101111 00101110"