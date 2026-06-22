def build_reverse_number_triangle(rows: int=5) -> list[str]:
    result = []
    for row_num in range(1, rows + 1):
        numbers = list(range(row_num, 0, -1))
        line = ' '.join((str(n) for n in numbers))
        result.append(line)
    return result
if __name__ == '__main__':
    for line in build_reverse_number_triangle(5):
        print(line)