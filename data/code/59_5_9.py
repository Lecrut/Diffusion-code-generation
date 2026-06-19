def find_middle_index(sequence):
    length = len(sequence)
    if length % 2 == 0:
        return length // 2 - 1
    else:
        return length // 2

if __name__ == '__main__':
    sample_list_odd = [1, 2, 3, 4, 5]
    sample_list_even = [1, 2, 3, 4, 5, 6]
    
    middle_index_odd = find_middle_index(sample_list_odd)
    middle_index_even = find_middle_index(sample_list_even)
    
    print(f"Middle index of odd length list: {middle_index_odd}")
    print(f"Middle index of even length list: {middle_index_even}")