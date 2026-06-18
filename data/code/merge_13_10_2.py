def main():
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print("Multiplication Table for a 3x3 Grid:")
    for i in range(3):
        for j in range(3):
            product = grid[i][j]
            print(f"Row {i+1}, Column {j+1}: {product}")
if __name__ == '__main__':
    main()