CHAR_COUNT_MAP = {
    'Hello, World!': 13,
    'Python': 6,
    'OpenAI': 6,
    '': 0,
    '1234567890': 10
}

def count_characters(text):
    return len(text)

if __name__ == '__main__':
    sample_text = "Hello, World!"
    print(count_characters(sample_text))