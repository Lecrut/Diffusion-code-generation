def fibonacci_sequence(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    else:
        sequence = [1, 1]
        for i in range(2, n):
            next_val = sequence[-1] + sequence[-2]
            sequence.append(next_val)
        return sequence
if __name__ == '__main__':
    n_terms = 10
    result = fibonacci_sequence(n_terms)
    print(result)