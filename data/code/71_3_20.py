class ListAnalyzer:
    MIDDLE_OFFSET = 0
    EVEN_LIST_DIVISOR = 2
    ODD_LIST_DIVISOR = 2
    EMPTY_LIST_RETURN = None
    INPUT_TYPE = list
    MIN_LENGTH = 1

    def __init__(self, data):
        if not isinstance(data, self.INPUT_TYPE):
            raise ValueError("Input must be a list")
        if len(data) < self.MIN_LENGTH:
            raise ValueError("List cannot be empty")
        self.data = data

    def get_middle_value(self):
        length = len(self.data)
        is_even = length % self.EVEN_LIST_DIVISOR == 0
        mid_index = length // self.ODD_LIST_DIVISOR
        if is_even:
            left_val = self.data[mid_index - 1]
            right_val = self.data[mid_index]
            return (left_val + right_val) / self.EVEN_LIST_DIVISOR
        return self.data[mid_index]

if __name__ == '__main__':
    sample_list_1 = [1, 2, 3, 4, 5]
    sample_list_2 = [10, 20, 30, 40]
    sample_list_3 = [7]
    analyzer_1 = ListAnalyzer(sample_list_1)
    print(analyzer_1.get_middle_value())
    analyzer_2 = ListAnalyzer(sample_list_2)
    print(analyzer_2.get_middle_value())
    analyzer_3 = ListAnalyzer(sample_list_3)
    print(analyzer_3.get_middle_value())