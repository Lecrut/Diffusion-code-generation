import operator
def find_max_iterative(data, key):
    if not data:
        raise ValueError("Input list cannot be empty")
    max_element = data[0]
    for item in data[1:]:
        if key(item) > key(max_element):
            max_element = item
    return max_element
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry", "date"]
    key1 = str
    max1 = find_max_iterative(list1, key1)
    print(f"List: {list1}, Max: {max1}")
    list2 = [3.14, 2.718, 1.618, 0.577]
    key2 = float
    max2 = find_max_iterative(list2, key2)
    print(f"List: {list2}, Max: {max2}")
    class CustomObject:
        def __init__(self, value):
            self.value = value
        def __lt__(self, other):
            return self.value < other.value
        def __gt__(self, other):
            return self.value > other.value
    obj_list = [CustomObject(10), CustomObject(50), CustomObject(30)]
    key3 = lambda x: x.value
    max3 = find_max_iterative(obj_list, key3)
    print(f"List: {obj_list}, Max Value: {max3.value}")
    empty_list = []
    try:
        find_max_iterative(empty_list, str)
    except ValueError as e:
        print(f"Error for empty list: {e}")