def get_middle_element(sequence):
    if not hasattr(sequence, '__len__'):
        raise TypeError("Input must be a sequence with a length.")
    if len(sequence) == 0:
        raise ValueError("Input sequence must not be empty.")
    
    length = len(sequence)
    if length % 2 == 1:
        return sequence[length // 2]
    else:
        return (sequence[length // 2 - 1] + sequence[length // 2]) / 2

if __name__ == '__main__':
    odd_list = [1, 2, 3, 4, 5]
    even_list = [1, 2, 3, 4]
    odd_tuple = (10, 20, 30)
    even_tuple = (10, 20, 30, 40)
    
    print(get_middle_element(odd_list))
    print(get_middle_element(even_list))
    print(get_middle_element(odd_tuple))
    print(get_middle_element(even_tuple))