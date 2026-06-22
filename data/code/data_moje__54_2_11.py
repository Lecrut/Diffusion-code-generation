def hollow_square(n):
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    if n == 2:
        return ['**', '**']
    
    full_line = '*' * n
    middle_lines = ['*' + ' ' * (n - 2) + '*'] * (n - 2)
    return [full_line] + middle_lines + [full_line]

if __name__ == '__main__':
    sample_n = 7
    result = hollow_square(sample_n)
    print('\n'.join(result))