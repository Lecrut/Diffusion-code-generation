class ListIterator:
    def __init__(self, input_list):
        self.input_list = input_list
        self.index = 0

    def get_next(self):
        if self.index < len(self.input_list):
            item = self.input_list[self.index]
            self.index += 1
            return f"{self.index - 1}: {item}"
        else:
            raise StopIteration

if __name__ == '__main__':
    sample_list = ['apple', 'banana', 'cherry']
    iterator = ListIterator(sample_list)
    print(iterator.get_next())
    print(iterator.get_next())
    print(iterator.get_next())