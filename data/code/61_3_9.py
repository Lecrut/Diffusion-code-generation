class ListElementExtractor:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index_five(self):
        try:
            return self.lst[4]
        except IndexError:
            raise ValueError("List does not have an element at index 5")

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    extractor = ListElementExtractor(sample_list)
    print(extractor.get_element_at_index_five())