def create_reverse_number_triangle(rows: int) -> list[str]:
    return [" ".join(str(i) for i in range(row, 0, -1)) for row in range(rows, 0, -1)]

if __name__ == "__main__":
    sample_rows = 5
    result = create_reverse_number_triangle(sample_rows)
    print(result)