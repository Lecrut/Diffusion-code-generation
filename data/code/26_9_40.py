class ListComparer:
    def __init__(self, lst):
        self.lst = lst

    def is_first_greater(self):
        return self.lst[0] > self.lst[1]

if __name__ == '__main__':
    sample_list = [5, 3]
    comparer = ListComparer(sample_list)
    print(comparer.is_first_greater())