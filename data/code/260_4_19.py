class StringComparator:
    def find_common_reversed(self, list1, list2):
        common_elements = set(list1) & set(list2)
        return list(common_elements)[::-1]

if __name__ == '__main__':
    comparator = StringComparator()
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    result = comparator.find_common_reversed(sample_list1, sample_list2)
    print(result)