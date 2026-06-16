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
    print(f"List 1: {list1}, Maximum: {find_maximum(list1)}")
    print(f"List 2: {list2}, Maximum: {find_maximum(list2)}")
    print(f"List 3: {list3}, Maximum: {find_maximum(list3)}")
    try:
        find_maximum(list4)
    except ValueError as e:
        print(f"List 4: {list4}, Error: {e}")