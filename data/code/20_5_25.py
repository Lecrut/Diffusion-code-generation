class MyClass:

    def __init__(self, value):
        self.value = value

    @classmethod
    def is_identical(cls, instance1, instance2):
        return cls._compare(instance1, instance2)

    @staticmethod
    def _compare(obj1, obj2):
        if type(obj1) != type(obj2):
            return False
        if isinstance(obj1, dict):
            return all((cls._compare(v1, v2) for k1, v1 in obj1.items() for k2, v2 in obj2.items() if k1 == k2))
        elif isinstance(obj1, (list, tuple)):
            return len(obj1) == len(obj2) and all((cls._compare(o1, o2) for o1, o2 in zip(obj1, obj2)))
        else:
            return obj1 == obj2
if __name__ == '__main__':
    instance1 = MyClass({'a': 1, 'b': [2, 3]})
    instance2 = MyClass({'a': 1, 'b': [2, 3]})
    instance3 = MyClass({'a': 1, 'b': [2, 4]})
    print(MyClass.is_identical(instance1, instance2))
    print(MyClass.is_identical(instance1, instance3))