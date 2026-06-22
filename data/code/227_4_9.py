def print_hollow_square(n):
    if n <= 0:
        return
    for i in range(n):
        line = ""
        for j in range(n):
            if i == 0 or i == n - 1 or j == 0 or j == n - 1:
                line += "*"
            else:
                line += " "
        print(line)

if __name__ == '__main__':
    size = 4
    print_hollow_square(size)