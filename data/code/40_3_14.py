def extract_first_letters(s: str) -> str: return ' '.join(word[0] if word else '' for word in s.split()) if s.strip() else ""

if __name__ == '__main__':
    print(extract_first_letters("Hello World Python Programming"))
    print(extract_first_letters(""))