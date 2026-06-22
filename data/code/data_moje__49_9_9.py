def print_star_square(size):
    line = '*' * size
    lines = [line for _ in range(size)]
    result = '\n'.join(lines)
    print(result)
    return result

if __name__ == '__main__':
    N = 12
    print_star_square(N)