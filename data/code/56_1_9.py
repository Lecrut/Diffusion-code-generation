def print_multiplication_table(limit=12):
    for i in range(1, limit + 1):
        for j in range(1, limit + 1):
            print(f"{i * j:4}", end="")
        print()

if __name__ == '__main__':
    print_multiplication_table()