if __name__ == '__main__':
    limit = 20
    sequence_length = 15
    modulus = 5
    for i in range(limit):
        number = (i % modulus) + 1
        print(number)