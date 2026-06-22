def find_middle_element(sequence):
    length = len(sequence)
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_odd_length_list = [10, 20, 30, 40, 50]
    sample_even_length_list = [7, 14, 21, 28, 35, 42]
    empty_list = []
    
    print("Middle element of odd length list:", find_middle_element(sample_odd_length_list))
    print("Middle element of even length list:", find_middle_element(sample_even_length_list))
    print("Middle element of empty list:", find_middle_element(empty_list))