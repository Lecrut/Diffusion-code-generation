def geometric_sequence(start, ratio, terms):
    return [start * (ratio ** i) for i in range(terms)]

if __name__ == '__main__':
    print(geometric_sequence(5, 3, 8))