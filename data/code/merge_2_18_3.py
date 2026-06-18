def reverse_sequence(sequence):
    if not sequence:
        return []
    reversed_list = [sequence[-1]] + reverse_sequence(sequence[:-1])
    return reversed_list
if __name__ == '__main__':
    sample_data = ['a', 'b', 'c', 'd']
    result = reverse_sequence(sample_data)
    print(result)