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
        def __init__(self, value):
            self.value = value
        def __repr__(self):
            return f"CustomObject({self.value})"
    list3 = [CustomObject(10), CustomObject(50), CustomObject(30)]
    def custom_object_comparison(a, b):
        return a.value > b.value
    max3 = find_max_iterative(list3, custom_object_comparison)
    print(f"\nList: {list3}")
    print(f"Maximum element (based on CustomObject value comparison): {max3}")