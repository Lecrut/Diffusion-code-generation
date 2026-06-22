def build_left_aligned_pyramid(rows=6):
    result = []
    for i in range(1, rows + 1):
        line = ' ' * (rows - i) + ' '.join(str(j) for j in range(1, i + 1))
        result.append(line)
    return result

if __name__ == '__main__':
    print(build_left_aligned_pyramid(6))