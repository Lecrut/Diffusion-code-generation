def generate_diagonal_pattern(n):
    if n <= 0:
        return []
    result = []
    for i in range(1, n + 1):
        row = [i]
        for j in range(1, i):
            row.append(j)
        result.extend(row[::-1])
    return result
if __name__ == '__main__':
    limit = 5
    pattern = generate_diagonal_pattern(limit)
    print(pattern)