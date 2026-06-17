import sys
def find_maximum(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_value = data[0]
    for number in data[1:]:
        if number > max_value:
            max_value = number
    return max_value
if __name__ == '__main__':
    list1 = [10, 5, 20, 8, 15]
    list2 = [-5, -1, -10, -3]
    list3 = [42]
    list4 = []
    print(f"Maximum of {list1}: {find_maximum(list1)}")
    print(f"Maximum of {list2}: {find_maximum(list2)}")
    print(f"Maximum of {list3}: {find_maximum(list3)}")
    try:
        print(f"Maximum of {list4}: {find_maximum(list4)}")
    except ValueError as e:
        print(f"Error for {list4}: {e}")