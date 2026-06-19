class MyClass:

    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    @classmethod
    def is_identical(cls, instance1, instance2):
        return cls.__dict__ == instance1.__dict__ == instance2.__dict__
if __name__ == '__main__':
    obj1 = MyClass(1, 2)
    obj2 = MyClass(1, 2)
    obj3 = MyClass(2, 1)
    print(MyClass.is_identical(obj1, obj2))
    print(MyClass.is_identical(obj1, obj3))