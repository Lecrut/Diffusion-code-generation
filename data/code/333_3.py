lambda s: "".join(char.upper() if char.isalpha() else char for char in s.split())
if __name__ == '__main__':
    input_string = "hello world this is a test"
    result = (lambda s: "".join(char.upper() if char.isalpha() else char for char in s.split()))(input_string)
    print(result)