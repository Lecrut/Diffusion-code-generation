def generate_nine_table_row(n):
    result = 9 * n
    return result

if __name__ == '__main__':
    start = 1
    end = 12
    current = start
    while current <= end:
        print(generate_nine_table_row(current))
        current += 1