class ElementCounter:
    @staticmethod
    def count_non_matching_elements(lst, cls):
        return sum(not isinstance(item, cls) for item in lst)

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', 3.14]
    result = ElementCounter.count_non_matching_elements(sample_list, int)
    print(result)