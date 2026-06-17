import operator
def find_max_iterative(data_list, comparison_func):
    if not data_list:
        raise ValueError("Input list cannot be empty")
    current_max = data_list[0]
    for item in data_list[1:]:
        if comparison_func(item, current_max):
            current_max = item
    return current_max
if __name__ == '__main__':
    list1 = ["apple", "banana", "cherry", "apricot"]
    def string_comparison(a, b):
        return a > b
    max1 = find_max_iterative(list1, string_comparison)
    print(f"List: {list1}")
    print(f"Maximum element (based on string comparison): {max1}")
    list2 = [3.14, 2.718, 1.618, 0.577]
    def float_comparison(a, b):
        return a > b
    max2 = find_max_iterative(list2, float_comparison)
    print(f"\nList: {list2}")
    print(f"Maximum element (based on float comparison): {max2}")
    class CustomObject:
        def __init__(self, name, value):
            self.name = name
            self.value = value
    obj_list = [CustomObject("A", 10), CustomObject("B", 50), CustomObject("C", 30)]
    def custom_object_comparison(obj_a, obj_b):
        return obj_a.value > obj_b.value
    max_obj = find_max_iterative(obj_list, custom_object_comparison)
    print(f"\nList of Custom Objects: {obj_list}")
    print(f"Maximum object (based on 'value'): {max_obj}")