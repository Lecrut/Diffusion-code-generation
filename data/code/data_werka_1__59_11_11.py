def find_middle_element(sequence):
    length = len(sequence)
    if length == 0:
        return None
    middle_index = length // 2
    return sequence[middle_index]

if __name__ == '__main__':
    sample_odd_list = [7, 14, 21, 28, 35]
    sample_even_list = [10, 20, 30, 40, 50, 60]
    sample_single_element = [42]
    sample_empty_list = []

    print(f"Middle element of odd list: {find_middle_element(sample_odd_list)}")
    print(f"Middle element of even list: {find_middle_element(sample_even_list)}")
    print(f"Middle element of single-element list: {find_middle_element(sample_single_element)}")
    print(f"Middle element of empty list: {find_middle_element(sample_empty_list)}")