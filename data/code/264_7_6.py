import re
def optimized_tokenizer(text: str) -> list[str]:
    tokens = re.findall(r'[a-zA-Z0-9]+', text)
    return tokens
if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, with various spaces and symbols... 123."
    sample_string_2 = "  leading space and trailing punctuation?  "
    sample_string_3 = "Word1, Word2;Word3"
    sample_string_4 = "Only_one_word"
    print(f"Input: '{sample_string_1}'")
    result_1 = optimized_tokenizer(sample_string_1)
    print(f"Output: {result_1}\n")
    print(f"Input: '{sample_string_2}'")
    result_2 = optimized_tokenizer(sample_string_2)
    print(f"Output: {result_2}\n")
    print(f"Input: '{sample_string_3}'")
    result_3 = optimized_tokenizer(sample_string_3)
    print(f"Output: {result_3}\n")
    print(f"Input: '{sample_string_4}'")
    result_4 = optimized_tokenizer(sample_string_4)
    print(f"Output: {result_4}\n")