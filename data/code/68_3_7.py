if __name__ == '__main__':
    A = [5, 10, 15]
    B = [3, 8, 12]
    differences = [a - b for a, b in zip(A, B)]
    print(differences)