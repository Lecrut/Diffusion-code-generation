class ListAnalyzer:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_first_value(self):
        if self.data_list:
            return self.data_list[0]
        else:
            return None

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())