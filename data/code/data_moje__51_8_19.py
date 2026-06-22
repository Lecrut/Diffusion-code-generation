def generate_number_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        row_str = ""
        for j in range(i):
            row_str += str(i)
        result.append(row_str)
    return result

if __name__ == '__main__':
    rows = 5
    pyramid = generate_number_pyramid(rows)
    for line in pyramid:
        print(line)