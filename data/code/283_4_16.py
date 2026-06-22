class ElementCounter:
    @staticmethod
    def count_non_matching_elements(lst, cls):
        if not isinstance(lst, list) or not all(isinstance(item, (list, dict, int, float, str)) for item in lst):
            raise ValueError("The first argument must be a list of elements.")
        if not issubclass(cls, object):
            raise TypeError("The second argument must be a class.")
        return sum(not isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', 3.0]
    result = ElementCounter.count_non_matching_elements(sample_list, int)
    print(result)