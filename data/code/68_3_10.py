def difference(A, B):
    return [a - b for a, b in zip(A, B)]

if __name__ == '__main__':
    A = [5, 10, 15]
    B = [2, 3, 8]
    print(difference(A, B))