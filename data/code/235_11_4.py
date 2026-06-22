def render_diamond(n):
    for i in range(2*n-1):
        if i < n:
            spaces = ' ' * (n - i - 1)
            stars = '*' * (2*i + 1)
        else:
            spaces = ' ' * (i - n + 1)
            stars = '*' * (4*n - 2*i - 3)
        print(spaces + stars)

if __name__ == '__main__':
    render_diamond(5)