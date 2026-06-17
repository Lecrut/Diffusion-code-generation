def to_uppercase_manual(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result
if __name__ == '__main__':
    input_string = "hello world"
    uppercase_string = to_uppercase_manual(input_string)
    print(uppercase_string)