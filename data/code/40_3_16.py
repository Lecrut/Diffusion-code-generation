def first_letters(s: str) -> str: return ' '.join(word[0] if word else '' for word in s.split())

if __name__ == '__main__':
    test_cases = ["hello world", "one two three four five six seven eight nine ten"]
    for tc in test_cases:
        print(f"Input: '{tc}' => Output: '{first_letters(tc)}'")