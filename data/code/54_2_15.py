def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    full_row = '*' * n
    hollow_row = '*' + ' ' * (n - 2) + '*'
    return [full_row] + [hollow_row] * (n - 2) + [full_row]

if __name__ == '__main__':
    sample_size = 5
    result = hollow_square(sample_size)
    for line in result:
        print(line)