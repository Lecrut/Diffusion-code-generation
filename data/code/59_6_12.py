def digit_sum(number):
    total = 0
    for char in str(number):
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(-98765))
    print(digit_sum(0))