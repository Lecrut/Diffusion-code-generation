class ListProcessor:
    def __init__(self, items):
        self.items = items

    def print_first_last(self):
        if self.items:
            print(f"First: {self.items[0]}, Last: {self.items[-1]}")
        else:
            print("List is empty")

if __name__ == '__main__':
    processor = ListProcessor([1, 2, 3, 4, 5])
    processor.print_first_last()