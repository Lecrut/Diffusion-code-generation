def print_inverted_alpha_triangle(start_char, rows):
    if rows <= 0 or not ('A' <= start_char <= 'Z'):
        return
    current_char_code = ord(start_char)
    for i in range(rows, 0, -1):
        line = ""
        for j in range(i):
            char_to_print = chr(current_char_code - j)
            if 'A' <= char_to_print <= 'Z':
                line += char_to_print + " "
            else:
                break
        if line:
            print(line.rstrip())
            current_char_code -= i
        else:
            break

if __name__ == '__main__':
    print_inverted_alpha_triangle('Z', 5)