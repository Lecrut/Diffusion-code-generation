def sum_digits(n):
    return sum(map(int, str(abs(n))))

if __name__ == '__main__':
    result = sum_digits(-12345)
    print(result)