def generate_hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['#']
    
    middle_row = '#' + '.' * (n - 2) + '#'
    rows = ['#' * n] + [middle_row for _ in range(n - 2)] + ['#' * n]
    return rows

if __name__ == '__main__':
    n = 5
    result = generate_hollow_square(n)
    print(result)
    for row in result:
        print(row)