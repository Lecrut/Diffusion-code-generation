def find_first_unique_char(s):
    frequency = {}
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    for char in s:
        if frequency[char] == 1:
            return char
    return None

if __name__ == '__main__':
    test_string = "swiss"
    result = find_first_unique_char(test_string)
    print(result)