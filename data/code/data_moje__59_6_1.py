def calculate_digit_sum(number):
    number_str = str(abs(number))
    digit_sum = 0
    for char in number_str:
        if char.isdigit():
            digit_sum += int(char)
    return digit_sum

if __name__ == '__main__':
    print(calculate_digit_sum(12345))
    print(calculate_digit_sum(-9876))
    print(calculate_digit_sum(0))
    print(calculate_digit_sum(1001))