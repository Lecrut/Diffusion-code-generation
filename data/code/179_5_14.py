def reverse_word_order(text: str) -> str:
    return ' '.join(text.split()[::-1])

if __name__ == '__main__':
    sample_string = "Python is awesome"
    result = reverse_word_order(sample_string)
    print(f"'{sample_string}' -> '{result}'")