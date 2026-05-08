class Sorter:
    def __init__(self, data):
        self.data = data
    def sort_data(self, reverse=True):
        self.data.sort(reverse=reverse)
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    sorter = Sorter(sample_list)
    sorter.sort_data()
    print(sorter.data)