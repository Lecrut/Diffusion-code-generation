import string

def count_special_characters(s):
    special_chars = string.punctuation
    count = 0
    status = False
    for char in s:
        if char in special_chars:
            count += 1
            status = True
    return count, status

if __name__ == '__main__':
    result = count_special_characters("Hello, World! @#")
    print(result)