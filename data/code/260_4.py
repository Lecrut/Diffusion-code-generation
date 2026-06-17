class NumberComparator:
    def compare(self, list_a, list_b):
        sum_a = sum(list_a)
        sum_b = sum(list_b)
        if sum_a >= sum_b:
            return list_a
        else:
            return list_b
if __name__ == '__main__':
    comparator = NumberComparator()
    list1 = [1, 5, 3]
    list2 = [2, 4, 1]
    result = comparator.compare(list1, list2)
    print(result)