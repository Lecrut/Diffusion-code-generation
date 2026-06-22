def construct_reverse_number_triangle(size):
    rows = []
    for i in range(size, 0, -1):
        row_numbers = list(range(1, i + 1))
        formatted = " ".join(str(num) for num in row_numbers)
        rows.append(formatted)
    return "\n".join(rows)

if __name__ == '__main__':
    sample_size = 5
    result = construct_reverse_number_triangle(sample_size)
    print(result)