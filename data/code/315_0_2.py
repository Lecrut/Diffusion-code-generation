if __name__ == '__main__':
    limit = 20
    sequence_length = 10
    divisor = 3
    for i in range(limit):
        number = (i % divisor) + 1
        print(number)