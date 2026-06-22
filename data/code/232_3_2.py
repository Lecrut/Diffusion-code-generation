def growing_number_sequence(n):
    return ','.join(str(i) for i in range(1, n + 1))

if __name__ == '__main__':
    N = 5
    result = growing_number_sequence(N)
    print(result)