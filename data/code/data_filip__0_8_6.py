def sum_of_digits(mixed_string):
    total = 0
    for char in mixed_string:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    test_string_1 = "abc123xyz45"
    test_string_2 = "no_digits_here"
    test_string_3 = "9a8b7c6d5e4f3g2h1i"
    
    print(sum_of_digits(test_string_1))
    print(sum_of_digits(test_string_2))
    print(sum_of_digits(test_string_3))