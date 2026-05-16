if __name__ == '__main__':
    A = [0, 0, 1, 1]
    B = [0, 1, 0, 1]
    print("A | B | A AND B")
    print("---|---|---------")
    for i in range(len(A)):
        result = A[i] and B[i]
        print(f"{A[i]} | {B[i]} | {result}")