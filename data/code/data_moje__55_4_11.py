def print_pyramid(max_height=5):
    rows = []
    for i in range(1, max_height + 1):
        spaces = ' ' * (max_height - i)
        chars = ' '.join([chr(64 + j) for j in range(1, i + 1)])
        rows.append(spaces + chars)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(print_pyramid(5))