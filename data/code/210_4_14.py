MIN_VALUE = -float('inf')
MAX_VALUE = float('inf')

def find_range(data):
    if not data:
        return None
    minimum = min(data, default=MIN_VALUE)
    maximum = max(data, default=MAX_VALUE)
    return (minimum, maximum)

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = []
    list3 = [10]
    list4 = [-5, 0, 5]
    print(f"Range of {list1}: {find_range(list1)}")
    print(f"Range of {list2}: {find_range(list2)}")
    print(f"Range of {list3}: {find_range(list3)}")
    print(f"Range of {list4}: {find_range(list4)}")