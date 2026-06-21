DELIMITER = ", "

def separate_characters(input_string):
    return DELIMITER.join(input_string)

if __name__ == '__main__':
    result1 = separate_characters("hello")
    print(result1)
    result2 = separate_characters("world")
    print(result2)
    result3 = separate_characters("")
    print(result3)