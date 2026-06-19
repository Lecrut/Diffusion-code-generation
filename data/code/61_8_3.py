class ElementFinder:
    def __init__(self, data_list):
        self.data_list = data_list

    def find_element_at_index(self, index):
        if 0 <= index < len(self.data_list):
            return self.data_list[index]
        else:
            raise IndexError("Index out of bounds")

if __name__ == '__main__':
    sample_data = [5, 15, 25, 35, 45]
    target_index = 3
    element_finder = ElementFinder(sample_data)
    try:
        result = element_finder.find_element_at_index(target_index)
        print(result)
    except IndexError as e:
        print(f"Error: {e}")