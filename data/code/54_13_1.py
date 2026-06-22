def hollow_square(n):
    return '\n'.join(['#' * n] + ['#' + ' ' * (n - 2) + '#' for _ in range(n - 2)] + ['#' * n] if n > 1 else ['#'] if n == 1 else '')

if __name__ == '__main__':
    print(hollow_square(5))