def sum_digits(number):
    return sum(map(int, str(number)))

if __name__ == '__main__':
    result = sum_digits(12345)
    print(result)