def generate_pyramid(rows: int) -> list[str]:
    return [f"{''.join(str(j) for j in range(1, i + 1))}" for i in range(1, rows + 1)]

if __name__ == '__main__':
    result = generate_pyramid(6)
    print(result)