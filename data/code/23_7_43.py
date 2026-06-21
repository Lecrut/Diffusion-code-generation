class ListComparer:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_sums(self):
        self.sum1 = sum(self.list1)
        self.sum2 = sum(self.list2)

    def compare_lists(self):
        if self.sum1 > self.sum2:
            return self.sum1, self.list1
        elif self.sum2 > self.sum1:
            return self.sum2, self.list2
        else:
            return self.sum1, None

def compare_and_report(list1, list2):
    comparer = ListComparer(list1, list2)
    comparer.calculate_sums()
    return comparer.compare_lists()

if __name__ == '__main__':
    list_a = [3, 4, 5, 6]
    list_b = [1, 2, 3, 4, 5]
    result = compare_and_report(list_a, list_b)
    print(result)

    list_c = [10, 20, 30]
    list_d = [5, 5, 5, 50]
    result2 = compare_and_report(list_c, list_d)
    print(result2)