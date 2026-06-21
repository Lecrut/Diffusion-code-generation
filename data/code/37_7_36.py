SPACE_SEPARATOR = " "

def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings.")
    return f"{str1}{SPACE_SEPARATOR}{str2}"

if __name__ == '__main__':
    sample_str_a = "Goodbye"
    sample_str_b = "Cruel World"
    result = combine_strings(sample_str_a, sample_str_b)
    print(result)