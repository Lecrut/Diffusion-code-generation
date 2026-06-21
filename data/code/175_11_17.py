import re

def clean_and_split(text):
    if not isinstance(text, str):
        raise ValueError("Input must be a string.")
    
    cleaned_text = re.sub(r'[^\w\s]', '', text)
    words = cleaned_text.split()
    return words

if __name__ == '__main__':
    long_text = "this is a very long sentence! designed to test the efficiency of word splitting on extremely long strings & ensure that the time complexity and space usage are minimal for large inputs."
    words = clean_and_split(long_text)
    print(words)