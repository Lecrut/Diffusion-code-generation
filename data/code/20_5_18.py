class MyClass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def is_identical(cls, instance1, instance2):
        return cls._compare(instance1.__dict__, instance2.__dict__)

    @staticmethod
    def _compare(dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False
        return True
if __name__ == '__main__':
    obj1 = MyClass(10)
    obj2 = MyClass(10)
    obj3 = MyClass(20)
    print(MyClass.is_identical(obj1, obj2))
    print(MyClass.is_identical(obj1, obj3))