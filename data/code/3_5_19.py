def remove_vowels(s: str) -> str:
    trans_table = str.maketrans('', '', 'aeiouAEIOU')
    return s.translate(trans_table)

if __name__ == '__main__':
    samples = [
        "Hello World",
        "Python Programming",
        "AEIOU aeio u",
        "No vowels here! 123",
        "",
        "a"
    ]
    for sample in samples:
        result = remove_vowels(sample)
        print(result)