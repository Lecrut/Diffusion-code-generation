def to_uppercase_manual(input_string):
    result = ""
    for char in input_string:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
if __name__ == '__main__':
    sample = "hello world"
    uppercase_result = to_uppercase_manual(sample)
    print(uppercase_result)