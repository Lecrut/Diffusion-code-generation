def print_right_aligned_triangle():
    count = 10
    lines = []
    for i in range(1, count + 1):
        line = '*' * i
        lines.append(line.rjust(count))
    for line in lines:
        print(line)

if __name__ == '__main__':
    print_right_aligned_triangle()