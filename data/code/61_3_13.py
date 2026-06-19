class ListExtractor:
    def __init__(self, lst):
        self.lst = lst

    def get_fifth_element(self):
        return self.lst[4]

if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50, 60]
    extractor = ListExtractor(sample_list)
    print(extractor.get_fifth_element())