def has_special_chars(s):
    for char in s:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample1 = "Hello World 123"
    sample2 = "Test@String!2023"
    sample3 = "Just letters and numbers"
    sample4 = "No specials here   "
    sample5 = "Special#Chars$Here%"
    
    result1 = has_special_chars(sample1)
    result2 = has_special_chars(sample2)
    result3 = has_special_chars(sample3)
    result4 = has_special_chars(sample4)
    result5 = has_special_chars(sample5)
    
    print(result1)
    print(result2)
    print(result3)
    print(result4)
    print(result5)