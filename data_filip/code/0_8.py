def sum_digits_in_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    print(sum_digits_in_string("abc123def45"))
    print(sum_digits_in_string("no_digits_here"))
    print(sum_digits_in_string("9g8f7e6d5c4b3a21"))
    print(sum_digits_in_string(""))
    print(sum_digits_in_string("100%"))