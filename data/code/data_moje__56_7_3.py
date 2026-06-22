def print_multiplication_table(base, start=1, end=10):
    width = len(str(base * end)) + 2
    for i in range(start, end + 1):
        product = base * i
        print(f"{i * base:>{width}}", end="")
        if i < end:
            print(",", end="")
        else:
            print()

if __name__ == '__main__':
    print_multiplication_table(12, 1, 10)