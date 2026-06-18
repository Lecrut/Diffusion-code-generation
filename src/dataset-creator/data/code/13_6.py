def simulate_multiplication_tables():
    for i in range(5, 11):
        print(f"--- Multiplication Table for {i} ---")
        for j in range(1, 11):
            product = i * j
            print(f"{i} x {j} = {product}")
        print()
if __name__ == '__main__':
    simulate_multiplication_tables()