ROWS = 5

def print_star_triangle(rows):
    pattern = '\n'.join(['*' * i for i in range(1, rows + 1)])
    return pattern

if __name__ == '__main__':
    result = print_star_triangle(ROWS)
    print(result)