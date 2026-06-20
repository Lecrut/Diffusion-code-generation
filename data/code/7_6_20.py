def has_special_chars(text):
    for char in text:
        if not char.isalnum() and not char.isspace():
            return True
    return False

if __name__ == '__main__':
    sample1 = "HelloWorld123"
    sample2 = "Hello@World!"
    sample3 = "   \t\n   "
    sample4 = "NoSpecChars123   "
    sample5 = "Has#Hash"
    
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