def sum_digits(number):
    return sum(map(int, str(number)))

if __name__ == '__main__':
    print(sum_digits(12345))