def generate_hollow_square(n: int) -> list[str]:
    if n <= 0:
        return []
    if n == 1:
        return ['*']
    top_bottom_row = '*' * n
    middle_row_template = '*' + ' ' * (n - 2) + '*'
    rows = []
    rows.append(top_bottom_row)
    for _ in range(n - 2):
        rows.append(middle_row_template)
    rows.append(top_bottom_row)
    return rows
if __name__ == '__main__':
    result = generate_hollow_square(5)
    print(result)
    result_3 = generate_hollow_square(3)
    print(result_3)
    result_1 = generate_hollow_square(1)
    print(result_1)
    result_0 = generate_hollow_square(0)
    print(result_0)