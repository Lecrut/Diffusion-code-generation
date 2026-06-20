def check_string(s):
    return "hello" in s or "world" in s

if __name__ == '__main__':
    print(check_string("hello world"))
    print(check_string("goodbye world"))
    print(check_string("hello universe"))
    print(check_string("world peace"))