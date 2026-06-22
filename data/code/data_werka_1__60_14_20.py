def get_last_element(arr):
    if not arr:
        return None
    return arr[-1]

if __name__ == '__main__':
    sample_array1 = [1, 2, 3, 4, 5]
    sample_array2 = []
    sample_array3 = ['a', 'b', 'c']
    
    print("Last element of sample_array1:", get_last_element(sample_array1))
    print("Last element of sample_array2:", get_last_element(sample_array2))
    print("Last element of sample_array3:", get_last_element(sample_array3))