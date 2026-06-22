def generate_left_aligned_number_pyramid(rows: int=6) -> list:
    result = []
    for i in range(1, rows + 1):
        row = ''.join((str(j) for j in range(1, i + 1)))
        result.append(row)
    return result
if __name__ == '__main__':
    pyramid = generate_left_aligned_number_pyramid(6)
    print(pyramid)