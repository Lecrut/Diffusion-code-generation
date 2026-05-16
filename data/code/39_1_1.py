import re
def extract_all_non_overlapping(text, pattern):
    return re.findall(pattern, text)
if __name__ == '__main__':
    input_string = "apple banana apple orange apple"
    pattern = r"\bapple\b"
    result = extract_all_non_overlapping(input_string, pattern)
    print(result)