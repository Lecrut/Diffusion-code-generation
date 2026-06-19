def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both inputs must be strings")
    return f"{str1} {str2}"

if __name__ == '__main__':
    try:
        sample_str1 = "Hello"
        sample_str2 = "Universe"
        result = combine_strings(sample_str1, sample_str2)
        print(result)
    except ValueError as e:
        print(e)