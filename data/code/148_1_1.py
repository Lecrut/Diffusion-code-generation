import sys
def find_largest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    largest = data[0]
    for i in range(1, len(data)):
        if data[i] > largest:
            largest = data[i]
    return largest
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2]
    list2 = [-10, -5, -20, -1]
    list3 = [42]
    list4 = [100, 50, 25, 75]
    list5 = []
    print(f"List 1: {list1}, Largest: {find_largest(list1)}")
    print(f"List 2: {list2}, Largest: {find_largest(list2)}")
    print(f"List 3: {list3}, Largest: {find_largest(list3)}")
    print(f"List 4: {list4}, Largest: {find_largest(list4)}")
    try:
        print(f"List 5: {list5}, Largest: {find_largest(list5)}")
    except ValueError as e:
        print(f"List 5: {list5}, Error: {e}")