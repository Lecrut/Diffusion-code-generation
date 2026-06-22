def digit_generator(n):
    s = str(abs(int(n)))
    for ch in s:
        yield int(ch)

def sum_digits(n):
    return sum(digit_generator(n))

if __name__ == '__main__':
    sample_number = 12345
    digits = list(digit_generator(sample_number))
    total = sum_digits(sample_number)
    print(digits)
    print(total)