def calculate_length_ratio(str1, str2):
    if len(str2) == 0:
        return float('inf') if len(str1) != 0 else 0
    return len(str1) / len(str2)

if __name__ == '__main__':
    string_a = "Hello, world!"
    string_b = "Goodbye!"
    ratio = calculate_length_ratio(string_a, string_b)
    print(ratio)