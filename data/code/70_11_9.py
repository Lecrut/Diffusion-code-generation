class ListEnds:
    @staticmethod
    def get_first_last(iterable):
        try:
            first = next(iter(iterable))
        except StopIteration:
            return None, None
        
        try:
            last = next(reversed(iterable))
        except StopIteration:
            return first, first
        
        return first, last

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    list2 = [10]
    list3 = []
    list4 = ['a', 'b']
    list5 = []

    print(f"List 1: {ListEnds.get_first_last(list1)}")
    print(f"List 2: {ListEnds.get_first_last(list2)}")
    print(f"List 3: {ListEnds.get_first_last(list3)}")
    print(f"List 4: {ListEnds.get_first_last(list4)}")
    print(f"List 5: {ListEnds.get_first_last(list5)}")