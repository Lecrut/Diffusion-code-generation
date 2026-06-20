import string

def find_first_special_char(text):
    special_chars = set(string.punctuation)
    for char in text:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Price: $100"
    sample3 = "abc!123"
    sample4 = "NoSpecialsHere"
    
    result1 = find_first_special_char(sample1)
    result2 = find_first_special_char(sample2)
    result3 = find_first_special_char(sample3)
    result4 = find_first_special_char(sample4)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)