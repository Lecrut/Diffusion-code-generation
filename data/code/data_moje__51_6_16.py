def generate_number_pyramid():
    levels = 4
    start_num = 1
    result = []

    for level in range(1, levels + 1):
        current_row = []
        for _ in range(level):
            current_row.append(start_num)
            start_num += 1
        result.append(current_row)

    return result

if __name__ == '__main__':
    pyramid = generate_number_pyramid()
    for row in pyramid:
        print(row)