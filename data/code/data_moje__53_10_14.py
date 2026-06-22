def generate_reverse_number_triangle(rows: int) -> list[str]:
    result = []
    for i in range(rows, 0, -1):
        row = " ".join(str(num) for num in range(i, 0, -1))
        result.append(row)
    return result

if __name__ == '__main__':
    sample_rows = 5
    print(generate_reverse_number_triangle(sample_rows))