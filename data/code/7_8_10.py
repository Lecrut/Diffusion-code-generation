def count_special_chars(s):
    count = 0
    found = False
    for char in s:
        if not char.isalnum() and not char.isspace():
            count += 1
            found = True
    return count, found

if __name__ == '__main__':
    result = count_special_chars("Hello, World! 123")
    print(result)
    result2 = count_special_chars("NoSpecialCharsHere")
    print(result2)
    result3 = count_special_chars("")
    print(result3)
    result4 = count_special_chars("!!!")
    print(result4)