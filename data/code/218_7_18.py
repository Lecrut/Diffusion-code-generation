def is_sorted(data):
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            return False
    return True

def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    if not is_sorted(data):
        raise ValueError("Input list must be sorted")
    return data[0]

if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    list2 = []
    list3 = [-10, -5, -20]
    try:
        result1 = find_minimum(list1)
        print(f"Minimum of {list1}: {result1}")
        result3 = find_minimum(list3)
        print(f"Minimum of {list3}: {result3}")
        find_minimum(list2)
    except ValueError as e:
        print(e)