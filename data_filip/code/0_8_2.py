def sum_digits_in_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    print(sum_digits_in_string("a1b2c3"))
    print(sum_digits_in_string("no digits here"))
    print(sum_digits_in_string("5test9data2"))