class MyClass:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    @classmethod
    def is_identical(cls, instance1, instance2):
        return cls.__dict__ == cls.__dict__ and instance1.__dict__ == instance2.__dict__
if __name__ == '__main__':
    obj1 = MyClass(10, 20)
    obj2 = MyClass(10, 20)
    obj3 = MyClass(10, 30)
    print(MyClass.is_identical(obj1, obj2))
    print(MyClass.is_identical(obj1, obj3))