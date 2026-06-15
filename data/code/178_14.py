import re
def split_string_basic(text):
    return text.split()
def split_string_regex(text):
    return re.findall(r'\S+|\s+', text)
if __name__ == '__main__':
    sample_string = "  Hello   world! How are you? "
    print("--- Basic Split ---")
    result_basic = split_string_basic(sample_string)
    print(result_basic)
    print("\n--- Regex Split (Preserving Spacing Context) ---")
    result_regex = split_string_regex(sample_string)
    print(result_regex)