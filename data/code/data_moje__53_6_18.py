def build_reverse_triangle(rows_count):
    row_strings = []
    current_row_index = rows_count
    while current_row_index > 0:
        segment_parts = []
        counter = current_row_index
        while counter > 0:
            segment_parts.append(str(current_row_index))
            counter -= 1
        row_strings.append(" ".join(segment_parts))
        current_row_index -= 1
    final_output = "\n".join(row_strings)
    return final_output

if __name__ == '__main__':
    sample_height = 4
    triangle_text = build_reverse_triangle(sample_height)
    print(triangle_text)