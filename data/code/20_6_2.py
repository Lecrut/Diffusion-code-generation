class ObjectComparator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
    def is_identical(self, other_instance):
        if not isinstance(other_instance, ObjectComparator):
            return False
        return self.value1 == other_instance.value1 and self.value2 == other_instance.value2
if __name__ == '__main__':
    obj1 = ObjectComparator(10, "hello")
    obj2 = ObjectComparator(10, "hello")
    obj3 = ObjectComparator(20, "world")
    print(f"obj1 is identical to obj2: {obj1.is_identical(obj2)}")
    print(f"obj1 is identical to obj3: {obj1.is_identical(obj3)}")
    print(f"obj2 is identical to obj1: {obj2.is_identical(obj1)}")
    print(f"obj3 is identical to obj1: {obj3.is_identical(obj1)}")
    print(f"obj1 is identical to obj1: {obj1.is_identical(obj1)}")