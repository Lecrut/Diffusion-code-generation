def create_symmetric_pyramid(levels):
    result = []
    for i in range(1, levels + 1):
        left_side = "".join(str(x) for x in range(1, i + 1))
        right_side = "".join(str(x) for x in range(i - 1, 0, -1))
        row = left_side + right_side
        result.append(row)
    return result

if __name__ == '__main__':
    sample_levels = 4
    output = create_symmetric_pyramid(sample_levels)
    for line in output:
        print(line)