def calculate_length_ratio(str1, str2):
    if len(str2) == 0:
        return float('inf') if len(str1) != 0 else 1.0
    return len(str1) / len(str2)

if __name__ == '__main__':
    string1 = "Hello, World!"
    string2 = "Goodbye!"
    ratio = calculate_length_ratio(string1, string2)
    print(ratio)