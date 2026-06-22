MAX_STRING_LENGTH = 100

def extract_first_letters(strings):
    first_letters = []
    for string in strings:
        if len(string) > MAX_STRING_LENGTH:
            raise ValueError("String length exceeds maximum allowed.")
        if string:
            first_letters.append(string[0])
    return first_letters

if __name__ == '__main__':
    sample_strings = ['watermelon', 'xigua', 'yam', 'zucchini']
    try:
        result = extract_first_letters(sample_strings)
        print(result)
    except ValueError as e:
        print(e)