class Comparator:
    TYPE_MISMATCH = "Type mismatch: Cannot directly compare {} and {}"
    SUPPORTED_TYPES = (int, str)

    @staticmethod
    def _compare(x, y):
        if x < y:
            return f"Comparison: {x} < {y}"
        elif x > y:
            return f"Comparison: {x} > {y}"
        else:
            return f"Comparison: {x} == {y}"

    @classmethod
    def compare_and_report(cls, x, y):
        if isinstance(x, cls.SUPPORTED_TYPES) and isinstance(y, cls.SUPPORTED_TYPES):
            if type(x) != type(y):
                raise TypeError(cls.TYPE_MISMATCH.format(type(x).__name__, type(y).__name__))
            return cls._compare(x, y)
        else:
            raise TypeError(cls.TYPE_MISMATCH.format(type(x).__name__, type(y).__name__))

if __name__ == '__main__':
    print("--- Integer Comparison ---")
    try:
        print(Comparator.compare_and_report(10, 5))
        print(Comparator.compare_and_report(20, 20))
        print(Comparator.compare_and_report(3, 1))
    except TypeError as e:
        print(e)

    print("--- String Comparison ---")
    try:
        print(Comparator.compare_and_report("apple", "banana"))
        print(Comparator.compare_and_report("grape", "grape"))
        print(Comparator.compare_and_report("melon", "kiwi"))
    except TypeError as e:
        print(e)