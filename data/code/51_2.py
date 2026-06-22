def generate_left_aligned_pyramid():
    rows = 6
    result = []
    for i in range(1, rows + 1):
        row_nums = [str(j) for j in range(1, i + 1)]
        result.append(' '.join(row_nums))
    return result

if __name__ == '__main__':
    pyramid = generate_left_aligned_pyramid()
    print(pyramid)