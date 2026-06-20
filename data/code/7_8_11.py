import string

def count_special_chars(s):
    count = 0
    found = False
    for char in s:
        if not char.isalnum() and char not in string.whitespace and char != '\n' and char != '\r' and char != '\t':
            count += 1
            found = True
    return count, found

if __name__ == '__main__':
    test_string = "Hello World! @Python#2023"
    result = count_special_chars(test_string)
    print(result)
    sample_text = "No special chars here"
    result2 = count_special_chars(sample_text)
    print(result2)
    empty_string = ""
    result3 = count_special_chars(empty_string)
    print(result3)