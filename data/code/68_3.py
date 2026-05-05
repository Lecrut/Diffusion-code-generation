if __name__ == '__main__':
    A = [1, 2, 3, 4]
    B = [5, 6, 7, 8]
    differences = [a - b for a, b in zip(A, B)]
    print(differences)