import re

def extract_digits_to_tuple(text: str) -> tuple:
    digits = re.findall(r'\d', text)
    return tuple(int(d) for d in digits)

if __name__ == '__main__':
    sample_text = "Error code 404 in file line 12: user_id 88 and retry 3 times."
    result = extract_digits_to_tuple(sample_text)
    print(result)