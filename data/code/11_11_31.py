def calculate_length_ratio(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    if len2 == 0:
        return float('inf')
    ratio = len1 / len2
    return ratio
if __name__ == '__main__':
    string1 = 'Hello, world!'
    string2 = 'Hello'
    result = calculate_length_ratio(string1, string2)
    print(result)