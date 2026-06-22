def calculate_average_of_pairs(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length")
    
    return [(a + b) / 2 for a, b in zip(list1, list2)]

if __name__ == '__main__':
    SAMPLE_LIST1 = [10, 20, 30]
    SAMPLE_LIST2 = [5, 15, 25]
    RESULT = calculate_average_of_pairs(SAMPLE_LIST1, SAMPLE_LIST2)
    print(RESULT)