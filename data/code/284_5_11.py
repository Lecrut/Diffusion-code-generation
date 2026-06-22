import random

class ListReverser:
    def __init__(self):
        self.reversed_list = []

    def reverse(self, lst):
        for i in range(len(lst)):
            self.reversed_list.insert(0, lst[i])

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [random.randint(1, 100) for _ in range(10)]
    print("Original list:", sample_list)
    reverser.reverse(sample_list)
    print("Reversed list:", reverser.reversed_list)