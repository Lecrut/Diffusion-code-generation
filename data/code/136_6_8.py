def check_string(s):
    return "apple" in s or "banana" in s

if __name__ == '__main__':
    print(check_string("I have an apple"))
    print(check_string("I have a banana"))
    print(check_string("I have a cherry"))