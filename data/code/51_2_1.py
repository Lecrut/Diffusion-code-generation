def generate_number_pyramid(rows: int = 6) -> list[str]:
    result = []
    for i in range(1, rows + 1):
        row_number = str(i)
        row_string = row_number.center(rows * 2 - 1)
        result.append(row_string)
    return result

if __name__ == '__main__':
    rows = 6
    pyramid = generate_number_pyramid(rows)
    for line in pyramid:
        print(line)