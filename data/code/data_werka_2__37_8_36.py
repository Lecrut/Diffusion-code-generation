def combine_strings(str1, str2):
    if not isinstance(str1, str) or not isinstance(str2, str):
        raise ValueError("Both arguments must be strings.")
    return f"{str1}{str2}"

if __name__ == '__main__':
    sample_values = [
        ("Hello", "World"),
        ("Python", "Programming")
    ]
    for str1, str2 in sample_values:
        result = combine_strings(str1, str2)
        print(result)