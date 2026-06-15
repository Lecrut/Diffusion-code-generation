import itertools
def generate_diagonal_pattern(n):
    if n <= 0:
        return []
    result = []
    for i in range(n):
        row = []
        for j in range(n):
            if i == j:
                row.append(i + 1)
            else:
                row.append(0)
        result.append(row)
    return result
if __name__ == '__main__':
    limit = 5
    pattern = generate_diagonal_pattern(limit)
    for row in pattern:
        print(row)