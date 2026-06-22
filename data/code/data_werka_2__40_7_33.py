import string

def extract_initials(input_string: str) -> list:
    PUNCTUATION_CHARS = set(string.punctuation)
    words = input_string.split()
    initials = []
    
    for word in words:
        stripped_word = ''.join(char for char in word if char not in PUNCTUATION_CHARS)
        if stripped_word:
            initials.append(stripped_word[0])
    
    return initials

if __name__ == '__main__':
    sample_input_1 = 'Hello, world! This is a test...'
    sample_input_2 = '...No words here!!!'
    sample_input_3 = 'Punctuation: should be ignored!'
    sample_input_4 = 'Numbers 123 and symbols @#$%^&*() are not words.'
    
    print(extract_initials(sample_input_1))
    print(extract_initials(sample_input_2))
    print(extract_initials(sample_input_3))
    print(extract_initials(sample_input_4))