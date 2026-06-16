import sys
def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    maximum = data[0]
    for number in data[1:]:
        if number > maximum:
            maximum = number
    return maximum
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -100, -3]
    list3 = [42]
    list4 = []
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {list3}: {find_maximum(list3)}")
    try:
        find_maximum(list4)
    except ValueError as e:
        print(f"Error for empty list: {e}")