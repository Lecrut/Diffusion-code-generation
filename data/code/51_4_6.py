def generate_pyramid():
    rows = []
    for i in range(1, 4):
        spaces = ' ' * (3 - i)
        numbers = ' '.join(str(i) for _ in range(i))
        rows.append(spaces + numbers + spaces)
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_pyramid())