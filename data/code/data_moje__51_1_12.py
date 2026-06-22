def create_symmetric_pyramid(levels):
    pyramid = []
    for i in range(1, levels + 1):
        space_count = levels - i
        left_side = "".join(str(x) for x in range(1, i))
        right_side = "".join(str(x) for x in range(i - 1, 0, -1))
        line = " " * space_count + str(i) + left_side + right_side
        pyramid.append(line)
    return "\n".join(pyramid)

if __name__ == '__main__':
    sample_levels = 4
    result = create_symmetric_pyramid(sample_levels)
    print(result)