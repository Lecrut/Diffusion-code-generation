def create_symmetric_pyramid(levels):
    result = []
    for i in range(1, levels + 1):
        left_side = "".join(str(j) for j in range(1, i + 1))
        right_side = "".join(str(j) for j in range(i - 1, 0, -1))
        result.append(left_side + right_side)
    return "\n".join(result)

if __name__ == '__main__':
    sample_levels = 4
    print(create_symmetric_pyramid(sample_levels))