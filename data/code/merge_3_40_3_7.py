def first_letters(s: str) -> str: return ' '.join([word[0] if word else '' for word in s.split()]) if any(word.strip() for word in s.split()) else ""

if __name__ == '__main__':
    print(first_letters("Hello world this is a test"))