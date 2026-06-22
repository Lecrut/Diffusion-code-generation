def diamond_pattern(n):
    middle = n // 2
    for i in range(n):
        if i <= middle:
            spaces = middle - i
            stars = 2 * i + 1
        else:
            spaces = i - middle
            stars = 2 * (n - i) + 1
        print(" " * spaces + "*" * stars)

if __name__ == '__main__':
    n_value = 5
    diamond_pattern(n_value)