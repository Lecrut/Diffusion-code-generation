def generate_number_pyramid(height: int) -> str:
    rows = []
    for i in range(1, height + 1):
        numbers = ' '.join(str(j) for j in range(1, i + 1))
        padding = ' ' * (height - i)
        rows.append(f"{padding}{numbers}")
    return '\n'.join(rows)

if __name__ == '__main__':
    print(generate_number_pyramid(7))