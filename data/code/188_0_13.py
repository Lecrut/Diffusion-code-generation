def reverse_list(arr):
    return arr[::-1]

if __name__ == '__main__':
    sample = [1, 2, 3, 4, 5]
    reversed_sample = reverse_list(sample)
    print("Original:", sample)
    print("Reversed:", reversed_sample)
    
    another_sample = [6, 7, 8, 9, 10]
    reversed_another_sample = reverse_list(another_sample)
    print("Original:", another_sample)
    print("Reversed:", reversed_another_sample)