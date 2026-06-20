def check_string(s):
    return "hello" in s or "world" in s

if __name__ == '__main__':
    sample_string = "Hello, world!"
    print(check_string(sample_string))