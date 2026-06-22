MAX_VALUE = float('-inf')

def find_maximum(numbers):
    return max(numbers, default=MAX_VALUE)

if __name__ == '__main__':
    sample_list1 = [1, 5, 2, 8, 3]
    print(f"Maximum of {sample_list1}: {find_maximum(sample_list1)}")
    sample_list2 = [-10, -5, -20, -1]
    print(f"Maximum of {sample_list2}: {find_maximum(sample_list2)}")