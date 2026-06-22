def get_middle_element(seq):
    n = len(seq)
    if n == 0:
        raise ValueError("Sequence must not be empty")
    if n % 2 == 1:
        return seq[n // 2]
    return (seq[n // 2 - 1], seq[n // 2])

if __name__ == '__main__':
    sample_tuple = (10, 20, 30, 40, 50)
    result = get_middle_element(sample_tuple)
    print(result)