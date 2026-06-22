import re

STARTING_LETTER = 'a'

def find_words_starting_with(text, letter):
    words = re.findall(r'\b\w+\b', text)
    return [word for word in words if word.lower().startswith(letter)]

if __name__ == '__main__':
    sample_text = "This is a sample sentence for finding words starting with 'a'. Another example: apple."
    result = find_words_starting_with(sample_text, STARTING_LETTER)
    print(result)