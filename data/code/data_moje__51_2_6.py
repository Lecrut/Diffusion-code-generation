def build_number_pyramid(rows):
    result = []
    for i in range(1, rows + 1):
        row_str = " ".join(str(num) for num in range(1, i + 1))
        result.append(row_str)
    return result

if __name__ == '__main__':
    pyramid = build_number_pyramid(6)
    print(pyramid)