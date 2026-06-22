class MyClass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def is_identical(cls, instance1, instance2):
        if not isinstance(instance1, cls) or not isinstance(instance2, cls):
            return False
        return instance1.__dict__ == instance2.__dict__
if __name__ == '__main__':
    obj1 = MyClass(42)
    obj2 = MyClass(42)
    obj3 = MyClass(43)
    print(MyClass.is_identical(obj1, obj2))
    print(MyClass.is_identical(obj1, obj3))