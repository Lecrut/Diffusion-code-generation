class StringComparator:
    def find_common_elements(self, list_a, list_b):
        return set(list_a) & set(list_b)

    def reverse_elements(self, elements):
        return list(elements)[::-1]

if __name__ == '__main__':
    comparator = StringComparator()
    sample_list1 = ['apple', 'banana', 'cherry']
    sample_list2 = ['banana', 'date', 'apple']
    common_elements = comparator.find_common_elements(sample_list1, sample_list2)
    reversed_common_elements = comparator.reverse_elements(common_elements)
    print(reversed_common_elements)