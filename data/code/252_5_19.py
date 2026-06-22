class QuantityComparer:
    DEFAULT_LIST1 = [1, 2, 3]
    DEFAULT_LIST2 = [4, 5, 6]

    @staticmethod
    def compare_sums(list1=DEFAULT_LIST1, list2=DEFAULT_LIST2):
        sum1 = sum(list1)
        sum2 = sum(list2)
        return sum1 == sum2

if __name__ == '__main__':
    comparer = QuantityComparer()
    result = comparer.compare_sums([7, 8], [9, 2])
    print(result)