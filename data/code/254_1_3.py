import random
def find_minimum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    minimum = data[0]
    for i in range(1, len(data)):
        if data[i] < minimum:
            minimum = data[i]
    return minimum
if __name__ == '__main__':
    list1 = [3, 1, 4, 1, 5, 9, 2, 6]
    print(f"List: {list1}")
    print(f"Minimum value: {find_minimum(list1)}")
    list2 = [-10, 5, -3, 8, 0]
    print(f"List: {list2}")
    print(f"Minimum value: {find_minimum(list2)}")
    list3 = [42]
    print(f"List: {list3}")
    print(f"Minimum value: {find_minimum(list3)}")
    list4 = [100, 50, 25, 75]
    print(f"List: {list4}")
    print(f"Minimum value: {find_minimum(list4)}")