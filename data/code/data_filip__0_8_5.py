def sum_digits_in_string(s):
    total = 0
    for char in s:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    sample1 = "a1b2c3"
    sample2 = "no digits here"
    sample3 = "12345"
    sample4 = "h3ll0 w0rld!"
    
    print(sum_digits_in_string(sample1))
    print(sum_digits_in_string(sample2))
    print(sum_digits_in_string(sample3))
    print(sum_digits_in_string(sample4))