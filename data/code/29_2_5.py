def count_vowels(text: str) -> int:
    vowels = set("aeiouAEIOU")
    count = 0
    for char in text:
        if char in vowels:
            count += 1
    return count

if __name__ == "__main__":
    sample_string_1 = "Hello World!"
    sample_string_2 = ""
    sample_string_3 = "AEIOUaeiou"
    sample_string_4 = "12345!@#"
    result_1 = count_vowels(sample_string_1)
    result_2 = count_vowels(sample_string_2)
    result_3 = count_vowels(sample_string_3)
    result_4 = count_vowels(sample_string_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)