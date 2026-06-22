def generate_hollow_square(size, border_char, interior_char):
    if size <= 0:
        return ""
    if size == 1:
        return border_char
    if size == 2:
        return border_char * 2 + "\n" + border_char * 2
    top_bottom = border_char * size
    middle_row = border_char + interior_char * (size - 2) + border_char
    middle_section = "\n".join([middle_row] * (size - 2))
    return top_bottom + "\n" + middle_section + "\n" + top_bottom

if __name__ == '__main__':
    sample_size = 5
    sample_border = "#"
    sample_interior = " "
    result = generate_hollow_square(sample_size, sample_border, sample_interior)
    print(result)