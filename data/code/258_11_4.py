def calculate_averages(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length")
    
    return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    sample_list1 = [10, 20, 30]
    sample_list2 = [5, 15, 25]
    print(calculate_averages(sample_list1, sample_list2))