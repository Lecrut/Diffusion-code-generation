class StringComparator:
    def find_common_reversed(self, list_a, list_b):
        common_elements = set(list_a) & set(list_b)
        return list(common_elements)[::-1]

if __name__ == '__main__':
    comparator = StringComparator()
    list1 = ['apple', 'banana', 'cherry']
    list2 = ['banana', 'date', 'apple']
    result = comparator.find_common_reversed(list1, list2)
    print(result)