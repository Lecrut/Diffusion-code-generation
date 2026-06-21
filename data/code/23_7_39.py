class ListComparer:

    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_sums(self):
        self.sum1 = sum(self.list1)
        self.sum2 = sum(self.list2)

    def compare_sums(self):
        if self.sum1 > self.sum2:
            return (self.sum1, self.list1)
        elif self.sum2 > self.sum1:
            return (self.sum2, self.list2)
        else:
            return (self.sum1, None)

def compare_and_report(list1, list2):
    comparer = ListComparer(list1, list2)
    comparer.calculate_sums()
    return comparer.compare_sums()
if __name__ == '__main__':
    list_a = [10, 20, 30, 40]
    list_b = [5, 15, 25]
    result = compare_and_report(list_a, list_b)
    print(result)
    list_c = [1, 1, 1, 1, 1]
    list_d = [2, 2, 2]
    result2 = compare_and_report(list_c, list_d)
    print(result2)
    list_e = [0, 0, 0]
    list_f = [0, 0, 0]
    result3 = compare_and_report(list_e, list_f)
    print(result3)