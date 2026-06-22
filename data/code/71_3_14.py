class ListAnalyzer:
    OFFSET = 0
    EVEN_LIST_DIVISOR = 2
    LIST_LENGTH_THRESHOLD = 0

    def __init__(self, data):
        if not isinstance(data, list):
            raise ValueError("Data must be a list")
        if len(data) == self.LIST_LENGTH_THRESHOLD:
            raise ValueError("List cannot be empty")
        self.data = data

    def get_middle_value(self):
        length = len(self.data)
        if length % self.EVEN_LIST_DIVISOR == 0:
            mid_index = length // self.EVEN_LIST_DIVISOR
            first_mid = self.data[mid_index - self.OFFSET]
            second_mid = self.data[mid_index]
            return (first_mid + second_mid) / self.EVEN_LIST_DIVISOR
        else:
            mid_index = length // self.EVEN_LIST_DIVISOR
            return self.data[mid_index]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    analyzer1 = ListAnalyzer(list1)
    print(analyzer1.get_middle_value())
    list2 = [10, 20, 30, 40]
    analyzer2 = ListAnalyzer(list2)
    print(analyzer2.get_middle_value())
    list3 = [7]
    analyzer3 = ListAnalyzer(list3)
    print(analyzer3.get_middle_value())