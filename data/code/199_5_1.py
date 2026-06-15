import random
class List:
    def __init__(self, items):
        self.items = items
    def shuffle(self):
        random.shuffle(self.items)
if __name__ == '__main__':
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    my_list = List(names)
    print("Original list:", my_list.items)
    my_list.shuffle()
    print("Shuffled list:", my_list.items)