def find_smallest(data):
    if not data:
        raise ValueError("Input list cannot be empty")
    smallest = data[0]
    for element in data[1:]:
        if element < smallest:
            smallest = element
    return smallest
if __name__ == '__main__':
    list1 = [5, 2, 8, 1, 9]
    print(f"The smallest element in {list1} is: {find_smallest(list1)}")
    list2 = [-10, 0, -5, 3]
    print(f"The smallest element in {list2} is: {find_smallest(list2)}")
    list3 = [42]
    print(f"The smallest element in {list3} is: {find_smallest(list3)}")
    list4 = [7]
    print(f"The smallest element in {list4} is: {find_smallest(list4)}")
    list5 = []
    try:
        print(f"The smallest element in {list5} is: {find_smallest(list5)}")
    except ValueError as e:
        print(f"Error for empty list: {e}")