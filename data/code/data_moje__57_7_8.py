def calculate_fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    sequence = [0, 1]
    for i in range(2, n):
        prev = sequence[-1]
        prev_prev = sequence[-2]
        sequence.append(prev + prev_prev)
    return sequence

if __name__ == '__main__':
    terms = calculate_fibonacci(100)
    for term in terms:
        print(term)