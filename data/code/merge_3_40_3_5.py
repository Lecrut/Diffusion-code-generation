def extract_first_letters(s: str) -> str: return ' '.join(word[0] if word else '' for word in s.split()) if any(c.isalpha() or c == '-' for c in s) else ''

if __name__ == '__main__':
    print(extract_first_letters("Hello, World! This is a test."))