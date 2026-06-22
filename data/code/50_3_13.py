def print_star_triangle(rows):
    line = ""
    for _ in range(rows):
        line += "*"
        print(line)

if __name__ == '__main__':
    print_star_triangle(15)