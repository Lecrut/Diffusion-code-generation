def generate_nine_table(limit):
    for i in range(1, limit + 1):
        print(f"9 x {i} = {9 * i}")

if __name__ == '__main__':
    generate_nine_table(10)