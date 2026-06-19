if __name__ == '__main__':
    A = [10, 20, 30]
    B = [5, 15, 25]
    differences = {f'element_{i}': a - b for i, (a, b) in enumerate(zip(A, B))}
    print(differences)