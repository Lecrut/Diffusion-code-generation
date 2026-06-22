class ListComparator:
    def __init__(self, lst):
        self.lst = lst

    def is_first_greater(self):
        return self.lst[0] > self.lst[1]

if __name__ == '__main__':
    sample_list = [9, 4]
    comparator = ListComparator(sample_list)
    print(comparator.is_first_greater())