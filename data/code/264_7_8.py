import re
def optimized_tokenize(text: str) -> list[str]:
    if not text:
        return []
    tokens = re.findall(r'[a-zA-Z0-9]+', text)
    return tokens
if __name__ == '__main__':
    sample_string_1 = "Hello world! This is a test, how are you?"
    sample_string_2 = "  Multiple   spaces \t and \n newlines\r.  "
    sample_string_3 = "Word123-with_symbols... and final."
    sample_string_4 = ""
    sample_string_5 = "  leading and trailing spaces "
    result_1 = optimized_tokenize(sample_string_1)
    print(f"Input: '{sample_string_1}'")
    print(f"Output: {result_1}\n")
    result_2 = optimized_tokenize(sample_string_2)
    print(f"Input: '{sample_string_2}'")
    print(f"Output: {result_2}\n")
    result_3 = optimized_tokenize(sample_string_3)
    print(f"Input: '{sample_string_3}'")
    print(f"Output: {result_3}\n")
    result_4 = optimized_tokenize(sample_string_4)
    print(f"Input: '{sample_string_4}'")
    print(f"Output: {result_4}\n")
    result_5 = optimized_tokenize(sample_string_5)
    print(f"Input: '{sample_string_5}'")
    print(f"Output: {result_5}\n")