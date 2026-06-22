def create_symmetric_pyramid(levels: int) -> str:
    if levels < 1:
        return ""
    
    result_lines = []
    for i in range(1, levels + 1):
        spaces = " " * (levels - i)
        left_side = "".join(str(k) for k in range(1, i + 1))
        right_side = "".join(str(k) for k in range(i - 1, 0, -1))
        line = spaces + left_side + right_side
        result_lines.append(line)
    
    return "\n".join(result_lines)

if __name__ == '__main__':
    sample_levels = 4
    pyramid_output = create_symmetric_pyramid(sample_levels)
    print(pyramid_output)