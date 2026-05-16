def calculate_phrase_length(phrase: str) -> int:
    return len(phrase)
if __name__ == '__main__':
    sample_phrase_1 = "Hello World"
    result_1 = calculate_phrase_length(sample_phrase_1)
    print(f"The length of '{sample_phrase_1}' is: {result_1}")
    sample_phrase_2 = "Python"
    result_2 = calculate_phrase_length(sample_phrase_2)
    print(f"The length of '{sample_phrase_2}' is: {result_2}")
    sample_phrase_3 = ""
    result_3 = calculate_phrase_length(sample_phrase_3)
    print(f"The length of '{sample_phrase_3}' is: {result_3}")
    sample_phrase_4 = "a" * 1000000
    result_4 = calculate_phrase_length(sample_phrase_4)
    print(f"The length of the long string is: {result_4}")