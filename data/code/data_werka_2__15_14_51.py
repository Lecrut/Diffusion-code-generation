class TypeSafeComparator:
    @staticmethod
    def compare(value1, value2):
        if isinstance(value1, (int, float)) and isinstance(value2, (int, float)):
            return TypeSafeComparator._compare_int_float(value1, value2)
        elif isinstance(value1, str) and isinstance(value2, str):
            return TypeSafeComparator._compare_str(value1, value2)
        elif isinstance(value1, list) and isinstance(value2, list):
            return TypeSafeComparator._compare_list(value1, value2)
        elif isinstance(value1, dict) and isinstance(value2, dict):
            return TypeSafeComparator._compare_dict(value1, value2)
        else:
            raise ValueError('Unsupported data types for comparison')

    @staticmethod
    def _compare_int_float(v1, v2):
        return v1 == v2

    @staticmethod
    def _compare_str(v1, v2):
        return v1.strip() == v2.strip()

    @staticmethod
    def _compare_list(v1, v2):
        if len(v1) != len(v2):
            return False
        for sub_v1, sub_v2 in zip(v1, v2):
            if not TypeSafeComparator.compare(sub_v1, sub_v2):
                return False
        return True

    @staticmethod
    def _compare_dict(v1, v2):
        if v1.keys() != v2.keys():
            return False
        for key in v1:
            if not TypeSafeComparator.compare(v1[key], v2[key]):
                return False
        return True

if __name__ == '__main__':
    print(TypeSafeComparator.compare(42, 42))
    print(TypeSafeComparator.compare(3.14, 3.14))
    print(TypeSafeComparator.compare(' hello ', 'hello'))
    print(TypeSafeComparator.compare([1, 2, 3], [1, 2, 3]))
    print(TypeSafeComparator.compare({'a': 1}, {'a': 1}))
    try:
        print(TypeSafeComparator.compare(42, '42'))
    except ValueError as e:
        print(e)