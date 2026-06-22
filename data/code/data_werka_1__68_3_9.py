if __name__ == '__main__':
    A = [5, 3, 9]
    B = [2, 1, 4]
    result = [a - b for a, b in zip(A, B)]
    print(result)