def calculate_phrase_length(phrase: str) -> int:
    return len(phrase)
if __name__ == '__main__':
    sample_phrase_1 = "hello world"
    result_1 = calculate_phrase_length(sample_phrase_1)
    print(f"Length of '{sample_phrase_1}': {result_1}")
    sample_phrase_2 = ""
    result_2 = calculate_phrase_length(sample_phrase_2)
    print(f"Length of '{sample_phrase_2}': {result_2}")
    sample_phrase_3 = "Python optimization"
    result_3 = calculate_phrase_length(sample_phrase_3)
    print(f"Length of '{sample_phrase_3}': {result_3}")