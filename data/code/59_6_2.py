def digit_sum(number: int) -> int:
    s = str(abs(number))
    total = 0
    for ch in s:
        total += int(ch)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(-987))
    print(digit_sum(0))