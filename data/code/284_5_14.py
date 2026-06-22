import random

class ListReverser:
    def __init__(self):
        self.reversed_list = []

    def add_to_reversed(self, item):
        self.reversed_list.insert(0, item)

    def get_reversed_list(self):
        return self.reversed_list

if __name__ == '__main__':
    reverser = ListReverser()
    sample_numbers = [random.randint(1, 100) for _ in range(10)]
    
    for number in sample_numbers:
        reverser.add_to_reversed(number)
    
    print("Reversed list:", reverser.get_reversed_list())