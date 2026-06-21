def get_central_item(sequence):
    if not sequence:
        raise ValueError('The sequence is empty')
    length = len(sequence)
    mid_index = length // 2
    if length % 2 == 0:
        return calculate_average(sequence[mid_index - 1], sequence[mid_index])
    else:
        return sequence[mid_index]

def calculate_average(a, b):
    return (a + b) / 2

if __name__ == '__main__':
    sample_sequence_odd = [15, 25, 35, 45, 55]
    sample_sequence_even = [10, 20, 30, 40, 50, 60]
    print(get_central_item(sample_sequence_odd))
    print(get_central_item(sample_sequence_even))