class StringComparator:
    @staticmethod
    def find_common_elements_reversed(list1, list2):
        common_elements = set(list1) & set(list2)
        return list(common_elements)[::-1]

if __name__ == '__main__':
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    result = StringComparator.find_common_elements_reversed(sample_list1, sample_list2)
    print(result)