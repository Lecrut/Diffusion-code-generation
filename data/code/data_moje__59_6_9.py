def digit_sum(number):
    if not isinstance(number, str):
        number = str(number)
    total = 0
    for char in number:
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(123))
    print(digit_sum("456"))
    print(digit_sum(0))
    print(digit_sum(987654321))