def digit_sum(n):
    total = 0
    for char in str(n):
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    number = 123456789
    result = digit_sum(number)
    print(result)