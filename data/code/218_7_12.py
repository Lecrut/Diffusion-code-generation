MIN_INDEX = 0

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    return data[MIN_INDEX]

if __name__ == '__main__':
    sample_list1 = [5, 2, 8, 1, 9]
    sample_list2 = []
    sample_list3 = [-10, -5, -20]
    try:
        result1 = find_minimum(sample_list1)
        print(f"Minimum of {sample_list1}: {result1}")
        result3 = find_minimum(sample_list3)
        print(f"Minimum of {sample_list3}: {result3}")
        find_minimum(sample_list2)
    except ValueError as e:
        print(e)