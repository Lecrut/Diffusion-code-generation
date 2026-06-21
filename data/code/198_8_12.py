class SortedList:

    def __init__(self, data):
        self.data = sorted(data)

    def get_smallest(self):
        if not self.data:
            raise ValueError('Input list cannot be empty')
        return self.data[0]
if __name__ == '__main__':
    sample_list = [5, 2, 8, 1]
    sorted_list_instance = SortedList(sample_list)
    smallest_item = sorted_list_instance.get_smallest()
    print(smallest_item)