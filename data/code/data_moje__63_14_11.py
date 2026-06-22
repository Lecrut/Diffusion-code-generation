def reverse_integer(n: int) -> int:
    if n < 0:
        return -int(''.join(reversed(list(str(abs(n))))))
    return int(''.join(reversed(list(str(n)))))

if __name__ == '__main__':
    sample_values = [123, -456, 7890, 0, 100]
    for value in sample_values:
        print(reverse_integer(value))