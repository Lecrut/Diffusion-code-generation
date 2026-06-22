def count_vowels(input_text: str) -> int:
    if not input_text:
        return 0
    vowel_set = frozenset('aeiouAEIOU')
    return sum(1 for char in input_text if char in vowel_set)

if __name__ == '__main__':
    sample_string = "Rhythm and Blues"
    result = count_vowels(sample_string)
    print(result)
    empty_string = ""
    empty_result = count_vowels(empty_string)
    print(empty_result)