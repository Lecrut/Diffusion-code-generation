def count_vowels(text: str) -> int:
    vowel_set = frozenset("aeiouAEIOU")
    total = 0
    for character in text:
        if character in vowel_set:
            total += 1
    return total

if __name__ == '__main__':
    test_string = "Encyclopedia"
    result = count_vowels(test_string)
    print(result)