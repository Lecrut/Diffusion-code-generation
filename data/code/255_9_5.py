def find_max_iterative(data_list, comparison_func):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    current_max = data_list[0]
    for i in range(1, len(data_list)):
        if comparison_func(data_list[i], current_max) > 0:
            current_max = data_list[i]
    return current_max
def compare_strings(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0
def compare_custom_objects(obj1, obj2):
    if obj1.value > obj2.value:
        return 1
    elif obj1.value < obj2.value:
        return -1
    else:
        return 0
if __name__ == '__main__':
    list_of_strings = ["apple", "zebra", "banana", "kiwi", "orange"]
    max_string = find_max_iterative(list_of_strings, compare_strings)
    print(f"List of strings: {list_of_strings}")
    print(f"Maximum string: {max_string}")
    class Item:
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return f"Item({self.value})"
    list_of_objects = [Item("cat"), Item("dog"), Item("elephant"), Item("mouse")]
    max_object = find_max_iterative(list_of_objects, compare_custom_objects)
    print(f"\nList of objects: {list_of_objects}")
    print(f"Maximum object: {max_object}")