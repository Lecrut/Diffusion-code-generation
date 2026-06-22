def reverse_alpha_triangle(start_char, end_char):
    start_ord = ord(start_char)
    end_ord = ord(end_char)
    if start_ord > end_ord:
        start_ord, end_ord = end_ord, start_ord
    char_range = list(range(start_ord, end_ord + 1))
    char_range.reverse()
    result = []
    width = len(char_range)
    for i in range(width):
        row_chars = []
        for j in range(i + 1):
            row_chars.append(chr(char_range[j]))
        result.append("".join(row_chars))
    return result

if __name__ == '__main__':
    sample_start = 'A'
    sample_end = 'F'
    lines = reverse_alpha_triangle(sample_start, sample_end)
    for line in lines:
        print(line)