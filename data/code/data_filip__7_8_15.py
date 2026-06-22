import string

def count_special_chars(s):
    count = 0
    found = False
    for char in s:
        if char in string.punctuation:
            count += 1
            found = True
    return (count, found)

if __name__ == '__main__':
    text = "Hello, World! 123."
    result = count_special_chars(text)
    print(result)