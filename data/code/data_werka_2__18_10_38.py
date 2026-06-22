def evaluate_first_greater_than_second(lst):
    return lst[0] > lst[1]

if __name__ == '__main__':
    SAMPLE_LIST_1 = [15, 10]
    SAMPLE_LIST_2 = [2, 3]
    SAMPLE_LIST_3 = [7.8, 7.8]
    
    print(f"Is the first element of {SAMPLE_LIST_1} greater than the second? {evaluate_first_greater_than_second(SAMPLE_LIST_1)}")
    print(f"Is the first element of {SAMPLE_LIST_2} greater than the second? {evaluate_first_greater_than_second(SAMPLE_LIST_2)}")
    print(f"Is the first element of {SAMPLE_LIST_3} greater than the second? {evaluate_first_greater_than_second(SAMPLE_LIST_3)}")