def generate_diagonal_pattern(limit):
    n = limit * limit
    pattern = [0] * n
    for i in range(limit):
        for j in range(limit):
            index = i + j * limit
            if index < n:
                pattern[index] = i + 1
    return pattern
if __name__ == '__main__':
    limit_val = 5
    result = generate_diagonal_pattern(limit_val)
    print(result)