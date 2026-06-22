def pyramid_pattern(n):
    for i in range(1, n + 1):
        spaces = " " * (n - i)
        line = spaces + "+".join(["+" * j for j in range(1, i + 1)]) + spaces
        print(line)

if __name__ == '__main__':
    pyramid_pattern(5)