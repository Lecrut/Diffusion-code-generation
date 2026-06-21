class ListReverser:
    def __init__(self, lst):
        self.lst = lst
    
    def reverse(self):
        return self.lst[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    reversed_list = reverser.reverse()
    print(reversed_list)

    another_sample = [10, 20, 30, 40, 50]
    another_reverser = ListReverser(another_sample)
    another_reversed_list = another_reverser.reverse()
    print(another_reversed_list)