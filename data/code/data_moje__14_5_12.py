def get_third_item(sequence):
    if len(sequence) < 3:
        raise ValueError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    print(get_third_item(sample_list))
    
    sample_string = "abcdef"
    print(get_third_item(sample_string))
    
    sample_tuple = (10, 20, 30, 40)
    print(get_third_item(sample_tuple))