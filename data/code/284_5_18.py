import random

class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list
        self.reversed_list = []

    def reverse(self):
        length = len(self.input_list)
        for i in range(length):
            self.reversed_list.append(self.input_list[length - 1 - i])

if __name__ == '__main__':
    sample_list = [random.randint(1, 100) for _ in range(10)]
    reverser = ListReverser(sample_list)
    reverser.reverse()
    print("Original list:", sample_list)
    print("Reversed list:", reverser.reversed_list)