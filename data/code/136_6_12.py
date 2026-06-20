def check_string(s):
    return "apple" in s or "banana" in s or s.startswith("fruit")

if __name__ == '__main__':
    print(check_string("I have an apple"))
    print(check_string("Banana is my favorite fruit"))
    print(check_string("This is a vegetable"))