def triangle_pattern(n):
    for i in range(1, n + 1):
        row = ['*'] * i
        yield ' '.join(row)

if __name__ == '__main__':
    pattern = list(triangle_pattern(5))
    print('\n'.join(pattern))