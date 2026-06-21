def get_third_item(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three items")
    return sequence[2]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    sample_string = "ABCDE"
    sample_tuple = (100, 200, 300)
    
    print(get_third_item(sample_list))
    print(get_third_item(sample_string))
    print(get_third_item(sample_tuple))