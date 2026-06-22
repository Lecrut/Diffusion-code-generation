class ElementCounter:
    @staticmethod
    def count_non_matching_elements(lst, cls):
        if not all(isinstance(item, (list, tuple)) for item in [lst, cls]):
            raise TypeError("Invalid input: lst must be a list and cls must be a class")
        return sum(not isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', 3.0]
    result = ElementCounter.count_non_matching_elements(sample_list, int)
    print(result)