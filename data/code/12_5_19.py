def get_middle(sequence):
    n = len(sequence)
    return sequence[n // 2]

if __name__ == '__main__':
    samples = [1, 2, 3, 4, 5]
    result = get_middle(samples)
    print(result)
    assert result == 3