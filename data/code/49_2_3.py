def print_star_square(n):
    line = '*' * n
    result = line + '\n'
    for _ in range(n - 1):
        result += line + '\n'
    result += line
    return result

if __name__ == '__main__':
    print(print_star_square(7))