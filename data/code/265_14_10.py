def check_same_characters(phrase1: str, phrase2: str) -> bool:
    return set(phrase1.replace(' ', '').lower()) == set(phrase2.replace(' ', '').lower())
if __name__ == '__main__':
    sample1 = 'Listen'
    sample2 = 'Silent'
    result = check_same_characters(sample1, sample2)
    print(result)
    sample3 = 'Hello World'
    sample4 = 'dlroW olleH'
    result = check_same_characters(sample3, sample4)
    print(result)
    sample5 = 'Python'
    sample6 = 'Java'
    result = check_same_characters(sample5, sample6)
    print(result)