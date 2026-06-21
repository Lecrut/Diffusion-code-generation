class ListProcessor:
    def __init__(self, lst):
        self.lst = lst

    def sort_and_find_middle(self):
        sorted_lst = sorted(self.lst)
        n = len(sorted_lst)
        if n % 2 == 0:
            return (sorted_lst[n // 2 - 1] + sorted_lst[n // 2]) / 2
        else:
            return sorted_lst[n // 2]

if __name__ == '__main__':
    processor1 = ListProcessor([1, 2, 3, 4, 5])
    print(processor1.sort_and_find_middle())

    processor2 = ListProcessor([10, 20, 30, 40])
    print(processor2.sort_and_find_middle())

    processor3 = ListProcessor([100])
    print(processor3.sort_and_find_middle())