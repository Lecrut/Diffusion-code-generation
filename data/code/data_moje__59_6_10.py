def digit_sum(n):
    s = str(n)
    total = 0
    for char in s:
        if char.isdigit() or (char == '-' and s.index(char) == 0):
            if char == '-':
                continue
            total += int(char)
    return total

if __name__ == '__main__':
    print(digit_sum(12345))
    print(digit_sum(-12345))
    print(digit_sum(0))