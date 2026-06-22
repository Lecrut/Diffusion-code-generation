def reverse_triangle(start_char, end_char):
    start_code = ord(start_char)
    end_code = ord(end_char)
    if start_code > end_code:
        start_code, end_code = end_code, start_code
    alphabet_segment = [chr(code) for code in range(start_code, end_code + 1)]
    alphabet_segment.reverse()
    result_lines = []
    length = len(alphabet_segment)
    for i in range(length):
        line = alphabet_segment[i]
        result_lines.append(line)
    return "\n".join(result_lines)

if __name__ == "__main__":
    sample_start = 'A'
    sample_end = 'E'
    print(reverse_triangle(sample_start, sample_end))