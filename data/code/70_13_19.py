class ListHandler:
    def __init__(self, items):
        self.items = items

    def print_first_last(self):
        if self.items:
            print(self.items[0], self.items[-1])
        else:
            print("List is empty")

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    handler = ListHandler(sample_list)
    handler.print_first_last()