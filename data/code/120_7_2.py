class MyObject:
    def __init__(self, value):
        self.value = value
    def __eq__(self, other):
        if isinstance(other, MyObject):
            return self.value == other.value
        return NotImplemented
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = [1, 2, 4]
def is_identical(obj1, obj2):
    return obj1 == obj2
result1 = is_identical(list1, list2)
result2 = is_identical(list1, list3)
if __name__ == '__main__':
    print(f"list1: {list1}")
    print(f"list2: {list2}")
    print(f"list3: {list3}")
    print(f"Is list1 identical to list2? {result1}")
    print(f"Is list1 identical to list3? {result2}")