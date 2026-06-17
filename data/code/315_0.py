if __name__ == '__main__':
    limit = 20
    sequence_length = 10
    for i in range(limit):
        number = (i % sequence_length) + 1
        print(number)