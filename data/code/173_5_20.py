class DataGrouper:
    def __init__(self):
        self.grouped_data = {}

    def group_by_first_element(self, nested_list):
        for sublist in nested_list:
            if sublist[0] not in self.grouped_data:
                self.grouped_data[sublist[0]] = []
            self.grouped_data[sublist[0]].extend(sublist[1:])

if __name__ == '__main__':
    sample_nested_list = [[1, 'a', 2], [3, 'b'], [1, 'c'], [4, 'd']]
    grouper = DataGrouper()
    grouper.group_by_first_element(sample_nested_list)
    
    for key, value in grouper.grouped_data.items():
        print(f"{key}: {value}")