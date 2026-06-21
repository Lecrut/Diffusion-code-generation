class ComplexObject:

    def __init__(self, data):
        self.data = data

    @classmethod
    def is_identical(cls, instance1, instance2):
        if not isinstance(instance1, cls) or not isinstance(instance2, cls):
            raise ValueError('Both instances must be of the same class')
        return cls._compare_dicts(instance1.__dict__, instance2.__dict__)

    @staticmethod
    def _compare_dicts(dict1, dict2):
        if len(dict1) != len(dict2):
            return False
        for key in dict1:
            if key not in dict2 or dict1[key] != dict2[key]:
                return False
        return True
if __name__ == '__main__':
    obj1 = ComplexObject([1, 2, 3])
    obj2 = ComplexObject([1, 2, 3])
    obj3 = ComplexObject([1, 2, 4])
    print(ComplexObject.is_identical(obj1, obj2))
    print(ComplexObject.is_identical(obj1, obj3))