class ListReverser:
    def __init__(self):
        self.internal_list = []
    def add_items(self, items):
        self.internal_list.extend(items)
    def reverse_and_return(self):
        reversed_list = self.internal_list[::-1]
        return reversed_list
if __name__ == '__main__':
    reverser = ListReverser()
    sample_data = [1, 2, 3, 4, 5]
    reverser.add_items(sample_data)
    result = reverser.reverse_and_return()
    print(result)