def calculate_length_ratio(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    
    if len2 == 0:
        return float('inf') if len1 != 0 else 0
    
    return len1 / len2

if __name__ == '__main__':
    string1 = "Hello, World!"
    string2 = "Python"
    ratio = calculate_length_ratio(string1, string2)
    print(ratio)