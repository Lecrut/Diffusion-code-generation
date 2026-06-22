def digit_sum(number):
    if not isinstance(number, int) and not isinstance(number, float):
        raise TypeError("Input must be a number")
    number_str = str(number)
    total = 0
    for char in number_str:
        if char.isdigit() or char == '-':
            if char.isdigit():
                total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(987654321))
    print(digit_sum(-42))
    print(digit_sum(0))
    print(digit_sum(1000000))