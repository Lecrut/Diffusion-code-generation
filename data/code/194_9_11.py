class StringFinder:
    NO_LONGEST_FOUND = None

    @staticmethod
    def is_iterable(obj):
        try:
            iter(obj)
            return True
        except TypeError:
            return False

    @staticmethod
    def longest_string(lst):
        if not StringFinder.is_iterable(lst):
            raise ValueError("Input must be an iterable")
        return max((s for s in lst if isinstance(s, str)), key=len, default=StringFinder.NO_LONGEST_FOUND)

if __name__ == '__main__':
    sample_list = ["apple", "banana", "cherry", 123, None]
    try:
        result = StringFinder.longest_string(sample_list)
        print(result)
    except ValueError as e:
        print(e)