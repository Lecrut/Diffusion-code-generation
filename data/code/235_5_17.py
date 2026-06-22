def print_triangle():
    for i in range(1, 6):
        line = ' '.join(str(j) for j in range(1, i + 1))
        print(line)

if __name__ == '__main__':
    print_triangle()