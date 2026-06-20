def check_string(s):
    return "apple" in s or "banana" in s or s.startswith("fruit")

if __name__ == '__main__':
    print(check_string("I have an apple"))
    print(check_string("Banana bread is delicious"))
    print(check_string("This is a fruit salad"))
    print(check_string("No fruits here"))