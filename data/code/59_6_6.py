def digit_sum(n):
    total = 0
    for char in str(n):
        if char.isdigit():
            total += int(char)
    return total

if __name__ == '__main__':
    result = digit_sum(12345)
    print(result)
    result2 = digit_sum(-987)
    print(result2)