lucas_sequence = {0: 2, 1: 1}

def generate_lucas(n):
    for i in range(2, n):
        lucas_sequence[i] = lucas_sequence[i-1] + lucas_sequence[i-2]
    return [lucas_sequence[i] for i in range(n)]

if __name__ == '__main__':
    sample_values = 9
    result = generate_lucas(sample_values)
    print(*result)