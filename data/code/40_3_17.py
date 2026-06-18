def extract_first_letters(s: str) -> str: return ' '.join(word[0] if (word := w.strip()) else '' for w in s.split() if word) or ''

if __name__ == '__main__':
    print(extract_first_letters("  Hello World Python Programming "))