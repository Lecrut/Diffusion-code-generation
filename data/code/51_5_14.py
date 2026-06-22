def generate_hollow_number_pyramid(rows=5):
    pattern = []
    for i in range(1, rows + 1):
        num_str = str(i)
        padding_count = i
        row = []
        for j in range(1, padding_count + 1):
            row.append(num_str)
        pattern.append(" ".join(row))
    return pattern

if __name__ == '__main__':
    result = generate_hollow_number_pyramid(5)
    print(result)