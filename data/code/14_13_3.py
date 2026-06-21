def get_third_element(sequence):
    if len(sequence) < 3:
        raise IndexError("Sequence must have at least three elements")
    return sequence[2]

if __name__ == "__main__":
    sample_list = [10, 20, 30, 40, 50]
    sample_tuple = ("apple", "banana", "cherry", "date")
    sample_string = "abcdefgh"
    
    print(get_third_element(sample_list))
    print(get_third_element(sample_tuple))
    print(get_third_element(sample_string))