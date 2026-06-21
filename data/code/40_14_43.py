def get_first_letter(s):
    if not isinstance(s, str) or len(s) == 0:
        raise ValueError("Input must be a non-empty string")
    return s[0]

if __name__ == '__main__':
    sample_string = "Alibaba Cloud"
    first_letter = get_first_letter(sample_string)
    print(first_letter)