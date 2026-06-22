def calculate_length_ratio(str1, str2):
    if len(str2) == 0:
        raise ValueError("The second string cannot be empty.")
    return len(str1) / len(str2)

if __name__ == '__main__':
    sample_str1 = "Hello, World!"
    sample_str2 = "Hello"
    ratio = calculate_length_ratio(sample_str1, sample_str2)
    print(ratio)