def generate_left_aligned_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        row_str = ''.join(str(j) for j in range(1, i + 1))
        result.append(row_str)
    return result

if __name__ == '__main__':
    print(generate_left_aligned_pyramid())