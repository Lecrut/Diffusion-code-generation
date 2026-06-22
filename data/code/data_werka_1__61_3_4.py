class ListElementExtractor:
    def __init__(self, lst):
        self.lst = lst

    def get_element_at_index_five(self):
        if len(self.lst) < 5:
            raise IndexError("List does not have an element at index 4.")
        return self.lst[4]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    extractor = ListElementExtractor(sample_list)
    try:
        print(extractor.get_element_at_index_five())
    except IndexError as e:
        print(e)