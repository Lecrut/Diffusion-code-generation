def digit_sum(number):
    number_str = str(number)
    total = 0
    for char in number_str:
        if char.isdigit() or char == '-':
            if char != '-':
                total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(-9876))
    print(digit_sum(0))
    print(digit_sum(100200300))