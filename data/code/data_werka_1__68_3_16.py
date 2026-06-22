if __name__ == '__main__':
    A = [20, 30, 40]
    B = [10, 20, 30]
    differences = {index: a - b for index, (a, b) in enumerate(zip(A, B))}
    print(differences)