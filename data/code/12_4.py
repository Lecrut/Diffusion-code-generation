import math

def get_middle_value(sequence):
    if not sequence:
        raise ValueError("Sequence must not be empty")
    
    n = len(sequence)
    sorted_seq = sorted(sequence)
    
    if n % 2 == 1:
        middle_index = n // 2
        return sorted_seq[middle_index]
    else:
        mid1 = n // 2 - 1
        mid2 = n // 2
        return (sorted_seq[mid1] + sorted_seq[mid2]) / 2

if __name__ == '__main__':
    odd_list = [1, 3, 2]
    even_list = [1, 3, 2, 4]
    single_element = [42]
    
    print(get_middle_value(odd_list))
    print(get_middle_value(even_list))
    print(get_middle_value(single_element))