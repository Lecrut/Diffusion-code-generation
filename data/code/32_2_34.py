def calculate_length(text):
    return len(text)

if __name__ == '__main__':
    sample_strings = {
        'greeting': 'Hello World',
        'empty': '',
        'short': 'Hi',
        'longer': 'Python programming'
    }
    for name, value in sample_strings.items():
        print(f"Length of '{value}': {calculate_length(value)}")