class MiddleItemFinder:
    def __init__(self, lst):
        if not lst:
            raise ValueError('The list is empty')
        self.lst = lst

    def find_middle_item(self):
        n = len(self.lst)
        middle_index = n // 2
        if n % 2 == 0:
            return (self.lst[middle_index - 1] + self.lst[middle_index]) / 2
        else:
            return self.lst[middle_index]

if __name__ == '__main__':
    sample_list_odd = [1, 3, 5, 7, 9]
    sample_list_even = [2, 4, 6, 8, 10, 12]

    finder_odd = MiddleItemFinder(sample_list_odd)
    print(finder_odd.find_middle_item())

    finder_even = MiddleItemFinder(sample_list_even)
    print(finder_even.find_middle_item())