def generate_number_pyramid(rows):
    return [
        f"{' '.join(str(i) for i in range(1, n + 1))}"
        .center(rows * 2 - 1)
        for n in range(1, rows + 1)
    ]

if __name__ == '__main__':
    rows = 7
    result = generate_number_pyramid(rows)
    print('\n'.join(result))