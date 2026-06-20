class DataSorter:
    def __init__(self):
        self.data = []

    def add_data(self, data):
        self.data.extend(data)

    def sort_data(self):
        return sorted(self.data, key=lambda x: (-x['primary'], x['secondary']))

if __name__ == '__main__':
    sorter = DataSorter()
    sample_data = [
        {'primary': 3, 'secondary': 2},
        {'primary': 1, 'secondary': 5},
        {'primary': 3, 'secondary': 1},
        {'primary': 2, 'secondary': 4},
        {'primary': 1, 'secondary': 3},
    ]
    sorter.add_data(sample_data)
    sorted_data = sorter.sort_data()
    for item in sorted_data:
        print(item)