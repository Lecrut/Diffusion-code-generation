def reverse_sequence(sequence):
    if not sequence:
        return []
    reversed_list = [sequence[-1]] + reverse_sequence(sequence[:-1])
    return reversed_list
if __name__ == '__main__':
    sample_data = [3, 6, 9]
    result = reverse_sequence(sample_data)
    print(result)