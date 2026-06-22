def digit_sum(number):
    number_str = str(number)
    total = 0
    for char in number_str:
        total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(987654321))
    print(digit_sum(0))
    print(digit_sum(1001))