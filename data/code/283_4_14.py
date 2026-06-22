class ElementCounter:
    @staticmethod
    def count_non_matching_elements(lst, cls):
        non_matching_count = 0
        for item in lst:
            if not isinstance(item, cls):
                non_matching_count += 1
        return non_matching_count

if __name__ == '__main__':
    sample_list = [1, 2.5, 'a', 'b', 3, 4]
    result = ElementCounter.count_non_matching_elements(sample_list, int)
    print(result)