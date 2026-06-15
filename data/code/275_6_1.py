class MySorter:
    def __init__(self, data):
        self.data = data
    def sort_in_place(self):
        self.data.sort()
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1, 9]
    sorter = MySorter(sample_list)
    sorter.sort_in_place()
    print(sample_list)