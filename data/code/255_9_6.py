def find_max_iterative(data_list, comparison_func):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    current_max = data_list[0]
    for item in data_list[1:]:
        if comparison_func(item, current_max) > 0:
            current_max = item
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
    list_of_strings = ["apple", "zebra", "banana", "grape", "kiwi"]
    max_string = find_max_iterative(list_of_strings, compare_strings)
    print(f"List of strings: {list_of_strings}")
    print(f"Maximum string: {max_string}")
    class Item:
        def __init__(self, value):
            self.value = value
    custom_objects = [Item("cat"), Item("dog"), Item("mouse"), Item("lion")]
    max_object = find_max_iterative(custom_objects, compare_custom_objects)
    print(f"List of custom objects: {custom_objects}")
    print(f"Maximum custom object (based on value): {max_object.value}")