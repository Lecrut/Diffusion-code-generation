class Sorter:
    def __init__(self):
        self.data = None
    def sort_data(self, data_list):
        self.data = data_list[::-1]
if __name__ == '__main__':
    sorter = Sorter()
    sample_list = [5, 2, 8, 1, 9]
    sorter.sort_data(sample_list)
    print(sorter.data)