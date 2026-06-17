def print_multiplication_table():
    for i in range(1, 6):
        for j in range(1, 11):
            print(f"{i} x {j}: {i * j:3d}", end=" | ")
        print()
if __name__ == '__main__':
    print_multiplication_table()