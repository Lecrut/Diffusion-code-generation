def extract_first_letters(s: str) -> str:
    return ' '.join(word[0] if word else '' for word in s.split())

if __name__ == '__main__':
    sample_input = "hello world python programming"
    result = extract_first_letters(sample_input)
    print(result)