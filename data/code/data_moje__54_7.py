def generate_hollow_square(n: int) -> list[str]:
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    solid_row = '*' * n
    middle_row = '*' + ' ' * (n - 2) + '*'
    result = []
    result.append(solid_row)
    for _ in range(n - 2):
        result.append(middle_row)
    result.append(solid_row)
    return result

if __name__ == '__main__':
    n = 5
    output = generate_hollow_square(n)
    print(output)