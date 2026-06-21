class ListAnalyzer:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_first_value(self):
        if not self.data_list:
            raise ValueError("The list is empty")
        return self.data_list[0]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())