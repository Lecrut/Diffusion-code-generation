def digit_sum(n: int) -> int:
    total = 0
    for ch in str(n):
        if ch == '-':
            continue
        total += int(ch)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(-678))
    print(digit_sum(0))