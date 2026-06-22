def print_centered_triangle(levels):
    for i in range(1, levels + 1):
        line = " " * (levels - i) + "* " * i
        print(line.strip())

if __name__ == '__main__':
    print_centered_triangle(12)