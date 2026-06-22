def get_multiplication_table_for_nine():
    return [f"9 x {i} = {9 * i}" for i in range(1, 11)]

if __name__ == '__main__':
    results = get_multiplication_table_for_nine()
    for line in results:
        print(line)