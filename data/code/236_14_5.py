from itertools import chain

class ListRepeater:
    def __init__(self, original_list):
        self.original = original_list

    def repeat(self, times):
        return list(chain.from_iterable([self.original] * times))

if __name__ == '__main__':
    repeater = ListRepeater([1, 2, 3])
    repeated_list = repeater.repeat(3)
    print(repeated_list)