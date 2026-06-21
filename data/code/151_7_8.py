import itertools

class ListInterleaver:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def interleave(self):
        return [item for sublist in itertools.zip_longest(self.list1, self.list2) for item in sublist if item is not None]

if __name__ == '__main__':
    interleaver = ListInterleaver([1, 3, 5], [2, 4, 6])
    result = interleaver.interleave()
    print(result)