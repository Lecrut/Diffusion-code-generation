import re
def extract_digits_count(s):
    return len(re.findall(r'\d', s))
if __name__ == '__main__':
    print(extract_digits_count("abc123def456"))
    print(extract_digits_count("no digits here"))
    print(extract_digits_count("9"))
    print(extract_digits_count(""))