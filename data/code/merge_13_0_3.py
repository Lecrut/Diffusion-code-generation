def demonstrate_multiplication():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    n = 3
    print("Demonstrating multiplication using nested loops for a 3x3 grid:")
    for i in range(n):
        for j in range(n):
            product = matrix[i][j] * 2
            print(f"Element at ({i}, {j}): {matrix[i][j]} * 2 = {product}")
if __name__ == '__main__':
    demonstrate_multiplication()