def sum_digits_from_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    print(sum_digits_from_string("abc123def45"))
    print(sum_digits_from_string("no digits here"))
    print(sum_digits_from_string("1a2b3c"))