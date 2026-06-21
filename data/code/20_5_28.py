class MyData:

    def __init__(self, data):
        self.data = data

    @classmethod
    def is_identical(cls, instance1, instance2):
        if not isinstance(instance1, cls) or not isinstance(instance2, cls):
            return False
        if instance1 is instance2:
            return True
        return instance1.data == instance2.data
if __name__ == '__main__':
    obj1 = MyData([1, 2, 3])
    obj2 = MyData([1, 2, 3])
    obj3 = MyData([1, 2, 4])
    print(MyData.is_identical(obj1, obj2))
    print(MyData.is_identical(obj1, obj3))