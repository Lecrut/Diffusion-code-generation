import string

def count_special_characters(s):
    special_chars = set(string.punctuation)
    count = 0
    for char in s:
        if char in special_chars:
            count += 1
    has_special = count > 0
    return count, has_special

if __name__ == '__main__':
    sample1 = "Hello, World!"
    sample2 = "NoSpecialCharsHere"
    sample3 = "@#$%^&*()"
    
    result1 = count_special_characters(sample1)
    result2 = count_special_characters(sample2)
    result3 = count_special_characters(sample3)
    
    print(result1)
    print(result2)
    print(result3)