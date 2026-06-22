LARGEST_INDEX = 0

def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest_index = LARGEST_INDEX
    for i in range(1, len(data)):
        if data[i] > data[largest_index]:
            largest_index = i
    return data[largest_index]

if __name__ == '__main__':
    list1 = [1, 5, 2, 8, 3]
    list2 = [-10, -5, -20, -1]
    list3 = [42]
    empty_list = []
    print(f"Largest in {list1}: {find_largest(list1)}")
    print(f"Largest in {list2}: {find_largest(list2)}")
    print(f"Largest in {list3}: {find_largest(list3)}")