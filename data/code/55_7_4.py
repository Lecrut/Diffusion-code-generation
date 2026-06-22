def reverse_triangle(start_char, end_char):
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    if start_ord > end_ord:
        start_ord, end_ord = end_ord, start_ord
    result_lines = []
    for i in range(start_ord, end_ord + 1):
        current_char = chr(i)
        line = []
        for j in range(end_ord, start_ord - 1, -1):
            if j >= i:
                line.append(chr(j))
            else:
                line.append(current_char)
        result_lines.append("".join(line))
    return "\n".join(result_lines)

if __name__ == '__main__':
    print(reverse_triangle('A', 'E'))