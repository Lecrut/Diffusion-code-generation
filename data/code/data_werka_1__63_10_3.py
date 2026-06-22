class ListAnalyzer:
    def __init__(self, lst):
        if not isinstance(lst, list):
            raise ValueError("Input must be a list")
        self.lst = lst

    def find_first_value(self):
        try:
            return self.lst[0]
        except IndexError:
            return None

if __name__ == '__main__':
    sample_list = [100, 200, 300, 400, 500]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())