import statistics

def get_median(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    return statistics.median(sequence)

if __name__ == '__main__':
    data = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    result = get_median(data)
    print(result)