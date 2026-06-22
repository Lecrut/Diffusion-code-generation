CHARACTER_COUNT_THRESHOLD = 100

def count_characters(text):
    if not isinstance(text, str):
        raise ValueError('Input must be a string')
    return sum((1 for char in text))
if __name__ == '__main__':
    sample_text1 = 'Hello, World!'
    sample_text2 = 'Python'
    sample_text3 = 'OpenAI'
    sample_text4 = ''
    sample_text5 = '1234567890' * 10
    print(count_characters(sample_text1))
    print(count_characters(sample_text2))
    print(count_characters(sample_text3))
    print(count_characters(sample_text4))
    print(count_characters(sample_text5))