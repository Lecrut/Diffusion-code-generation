def generate_reverse_number_triangle(height):
    lines = []
    for i in range(height, 0, -1):
        line = ""
        for j in range(i):
            line += str(i)
        lines.append(line)
    return lines

def print_reverse_number_triangle(height):
    lines = generate_reverse_number_triangle(height)
    for line in lines:
        print(line)

if __name__ == '__main__':
    height = 5
    print_reverse_number_triangle(height)