def create_symmetric_pyramid(levels=4):
    result = []
    for i in range(1, levels + 1):
        left_side = "".join(str(j) for j in range(1, i))
        center = str(i)
        right_side = "".join(str(j) for j in range(i - 1, 0, -1))
        line = left_side + center + right_side
        result.append(line)
    return "\n".join(result)

if __name__ == '__main__':
    print(create_symmetric_pyramid(4))