def hollow_square(n): return '\n'.join(['*' * n if r in (0, n - 1) else '*' + ' ' * (n - 2) + '*' if n > 1 else '*' for r in range(n)]) if n > 0 else ''

if __name__ == '__main__': print(hollow_square(5))