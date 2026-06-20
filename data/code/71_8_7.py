class ListWithMiddle:

    def __init__(self, elements):
        self.elements = elements

    def get_middle(self):
        length = len(self.elements)
        if length % 2 == 0:
            return None
        else:
            return self.elements[length // 2]
if __name__ == '__main__':
    sample_list = ListWithMiddle([1, 2, 3, 4, 5])
    print(sample_list.get_middle())
    sample_list = ListWithMiddle([10, 20, 30, 40])
    print(sample_list.get_middle())