def word_length_distribution(text: str) -> dict[int, list[str]]:
    words = text.split()
    distribution = {}
    for word in words:
        length = len(word)
        if length not in distribution:
            distribution[length] = []
        distribution[length].append(word)
    return distribution

if __name__ == '__main__':
    sample_text_1 = "Hello world! This is a test, how are you?"
    sample_text_2 = "  Multiple   spaces\tand\nnewlines\nwith punctuation... "
    sample_text_3 = "Word123-with_hyphens and $symbols."
    sample_text_4 = ""
    sample_text_5 = "OnlyWords"

    print(f"Input: '{sample_text_1}'")
    result_1 = word_length_distribution(sample_text_1)
    print(f"Output: {result_1}\n")

    print(f"Input: '{sample_text_2}'")
    result_2 = word_length_distribution(sample_text_2)
    print(f"Output: {result_2}\n")

    print(f"Input: '{sample_text_3}'")
    result_3 = word_length_distribution(sample_text_3)
    print(f"Output: {result_3}\n")

    print(f"Input: '{sample_text_4}'")
    result_4 = word_length_distribution(sample_text_4)
    print(f"Output: {result_4}\n")

    print(f"Input: '{sample_text_5}'")
    result_5 = word_length_distribution(sample_text_5)
    print(f"Output: {result_5}\n")