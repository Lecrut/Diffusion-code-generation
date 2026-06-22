class ElementCounter:
    @staticmethod
    def count_non_matching_elements(lst, cls):
        non_matching_count = sum(not isinstance(item, cls) for item in lst)
        return non_matching_count

if __name__ == '__main__':
    sample_list = [1, 2, 'a', 'b', 3.0]
    result = ElementCounter.count_non_matching_elements(sample_list, int)
    print(result)