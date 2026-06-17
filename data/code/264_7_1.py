import re
def highly_optimized_tokenize(text: str) -> list[str]:
    if not text:
        return []
    tokens = re.findall(r'\w+', text)
    return tokens
if __name__ == '__main__':
    sample_string_1 = "  Hello world! This is a test, how are you? "
    sample_string_2 = "Tokenization optimization is key for string processing."
    sample_string_3 = "123-abc@def 456"
    sample_string_4 = ""
    sample_string_5 = "   leading and trailing spaces   "
    print(f"Input: '{sample_string_1}'")
    result_1 = highly_optimized_tokenize(sample_string_1)
    print(f"Output: {result_1}\n")
    print(f"Input: '{sample_string_2}'")
    result_2 = highly_optimized_tokenize(sample_string_2)
    print(f"Output: {result_2}\n")
    print(f"Input: '{sample_string_3}'")
    result_3 = highly_optimized_tokenize(sample_string_3)
    print(f"Output: {result_3}\n")
    print(f"Input: '{sample_string_4}'")
    result_4 = highly_optimized_tokenize(sample_string_4)
    print(f"Output: {result_4}\n")
    print(f"Input: '{sample_string_5}'")
    result_5 = highly_optimized_tokenize(sample_string_5)
    print(f"Output: {result_5}\n")