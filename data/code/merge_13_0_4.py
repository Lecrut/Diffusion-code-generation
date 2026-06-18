def demonstrate_multiplication():
    grid_size = 3
    print("Demonstrating multiplication using nested loops for a 3x3 grid.")
    for i in range(grid_size):
        for j in range(grid_size):
            product = i * j
            print(f"Grid position ({i}, {j}): Product = {product}")
if __name__ == '__main__':
    demonstrate_multiplication()