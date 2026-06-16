def compare_string_lengths(str1, str2):
    return len(str1) - len(str2)
if __name__ == '__main__':
    string_a = "hello"
    string_b = "world"
    try:
        length_difference = compare_string_lengths(string_a, string_b)
        print(f"Length difference between '{string_a}' and '{string_b}': {length_difference}")
    except Exception as e:
        print(f"An error occurred: {e}")