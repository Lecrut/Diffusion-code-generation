def create_symmetric_pyramid(levels):
    lines = []
    mid = levels // 2 + (levels % 2)
    for i in range(1, levels + 1):
        num_str = str(i)
        if i <= mid:
            padding = (levels - i) * 2
            left_part = " ".join(str(j) for j in range(1, i + 1))
            right_part = " ".join(str(j) for j in range(i, 0, -1))
            line = left_part + right_part[1:]
            lines.append(" " * padding + line)
        else:
            padding = (i - mid - 1) * 2
            current_level = levels - (i - mid)
            left_part = " ".join(str(j) for j in range(1, current_level + 1))
            right_part = " ".join(str(j) for j in range(current_level, 0, -1))
            line = left_part + right_part[1:]
            lines.append(" " * padding + line)
    return "\n".join(lines)

if __name__ == '__main__':
    print(create_symmetric_pyramid(4))