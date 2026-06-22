def hollow_square(n):
    if n <= 0:
        return ""
    edge = '#' * n
    inner = '#' + ' ' * (n - 2) + '#' if n > 2 else '#'
    return '\n'.join([edge] + [inner] * (n - 2) + [edge] if n > 1 else [edge])

if __name__ == '__main__':
    print(hollow_square(5))
    print(hollow_square(2))
    print(hollow_square(1))
    print(hollow_square(0))