import re
def optimized_tokenizer(text: str) -> list[str]:
    if not text:
        return []
    tokens = re.findall(r'\w+', text)
    return tokens
if __name__ == '__main__':
    sample_string_1 = "  Hello, world! This is a test string with various - symbols. "
    sample_string_2 = "Word1, Word2;Word3\t\nAnother line here."
    sample_string_3 = "   leading and trailing spaces   "
    sample_string_4 = ""
    sample_string_5 = "OnlyWords"
    print(f"Input 1: '{sample_string_1}'")
    result_1 = optimized_tokenizer(sample_string_1)
    print(f"Result 1: {result_1}\n")
    print(f"Input 2: '{sample_string_2}'")
    result_2 = optimized_tokenizer(sample_string_2)
    print(f"Result 2: {result_2}\n")
    print(f"Input 3: '{sample_string_3}'")
    result_3 = optimized_tokenizer(sample_string_3)
    print(f"Result 3: {result_3}\n")
    print(f"Input 4: '{sample_string_4}'")
    result_4 = optimized_tokenizer(sample_string_4)
    print(f"Result 4: {result_4}\n")
    print(f"Input 5: '{sample_string_5}'")
    result_5 = optimized_tokenizer(sample_string_5)
    print(f"Result 5: {result_5}\n")