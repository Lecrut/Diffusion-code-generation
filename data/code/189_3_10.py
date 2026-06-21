class ListFilter:
    def __init__(self, data):
        self.data = data

    def filter_element(self, element_to_remove):
        return list((item for item in self.data if item != element_to_remove))

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5, 3]
    filter_instance = ListFilter(sample_list)
    filtered_list = filter_instance.filter_element(3)
    print(filtered_list)