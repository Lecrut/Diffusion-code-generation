def generate_hollow_square(n, border='#'):
    if n <= 0:
        return []
    if n == 1:
        return [border]
    first_row = border * n
    middle_row = border + ' ' * (n - 2) + border
    result = [first_row]
    for _ in range(n - 2):
        result.append(middle_row)
    result.append(first_row)
    return result

if __name__ == '__main__':
    pattern = generate_hollow_square(5, '*')
    for line in pattern:
        print(line)