def generate_pattern(rows, cols):
    for i in range(rows):
        for j in range(cols):
            print("*", end="")
        print()
if __name__ == '__main__':
    num_rows = 5
    num_cols = 10
    generate_pattern(num_rows, num_cols)