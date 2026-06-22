def sum_digits(n):
    return sum(map(int, str(abs(n))))

if __name__ == '__main__':
    print(sum_digits(12345))