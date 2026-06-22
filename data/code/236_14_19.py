from itertools import chain

class ListRepeater:
    def __init__(self, initial_list):
        self.initial_list = initial_list
    
    @staticmethod
    def concatenate_list(original, n):
        return list(chain.from_iterable([original] * n))
    
if __name__ == '__main__':
    repeater = ListRepeater([1, 2, 3])
    result = repeater.concatenate_list(repeater.initial_list, 3)
    print(result)