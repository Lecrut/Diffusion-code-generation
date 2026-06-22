def generate_right_aligned_reverse_triangle(n):
    lines = []
    for i in range(n, 0, -1):
        row_nums = [str(j) for j in range(i, 0, -1)]
        row_str = " ".join(row_nums)
        max_width = sum(len(str(j)) for j in range(n, 0, -1)) + n - 1
        lines.append(row_str.rjust(max_width))
    return "\n".join(lines)

if __name__ == '__main__':
    print(generate_right_aligned_reverse_triangle(4))