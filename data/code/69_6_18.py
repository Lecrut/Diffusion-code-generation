class ListDict:

    def __init__(self, lst):
        self.lst = lst

    def __getitem__(self, key):
        return self.lst[key]

    def __setitem__(self, key, value):
        self.lst[key] = value

    def __delitem__(self, key):
        del self.lst[key]

    def __len__(self):
        return len(self.lst)

    def __iter__(self):
        return iter(self.lst)
if __name__ == '__main__':
    ld = ListDict([10, 20, 30])
    print(ld[0])
    ld[1] = 25
    print(ld)
    del ld[2]
    print(len(ld))