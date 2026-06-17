def repeat_sequence(sequence, n):
    result = []
    for _ in range(n):
        result.extend(sequence)
    return result
if __name__ == '__main__':
    sequence = [1, 2]
    n = 3
    output = repeat_sequence(sequence, n)
    print(output)