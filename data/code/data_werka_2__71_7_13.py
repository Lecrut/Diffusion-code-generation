def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence with length")
    length = len(sequence)
    if length == 0:
        return None
    if length < 1:
        raise ValueError("Sequence must contain at least one element")
    midpoint = length // 2
    if length % 2 == 0:
        val1 = sequence[midpoint - 1]
        val2 = sequence[midpoint]
        return (val1 + val2) / 2.0
    return sequence[midpoint]

if __name__ == '__main__':
    odd_list = [10, 20, 30, 40, 50]
    even_list = [10, 20, 30, 40, 50, 60]
    single_list = [42]
    
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(single_list))