class ListWithMiddle:

    def __init__(self, elements):
        self.elements = elements

    def get_middle(self):
        length = len(self.elements)
        if length == 0:
            raise IndexError('List is empty')
        middle_index = (length - 1) // 2
        return self.elements[middle_index]
if __name__ == '__main__':
    sample_list = ListWithMiddle([1, 2, 3, 4, 5])
    print(sample_list.get_middle())