def print_hollow_square(side):
    if side == 1:
        return "X"
    if side < 1:
        return ""
    
    line_full = "X" * side
    line_middle = "X" + " " * (side - 2) + "X"
    
    lines = [line_full]
    for _ in range(side - 2):
        lines.append(line_middle)
    lines.append(line_full)
    
    return "\n".join(lines)

if __name__ == '__main__':
    side_length = 5
    print(print_hollow_square(side_length))