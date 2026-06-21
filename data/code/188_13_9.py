class ListReverser:
    @staticmethod
    def reverse(iterable):
        return iterable[::-1]

if __name__ == '__main__':
    list1 = [1, 2, 3, 4, 5]
    print(f"Original: {list1}, Reversed: {ListReverser.reverse(list1)}")
    list2 = ['a', 'b', 'c']
    print(f"Original: {list2}, Reversed: {ListReverser.reverse(list2)}")
    empty_list = []
    print(f"Original: {empty_list}, Reversed: {ListReverser.reverse(empty_list)}")
    list3 = [10, 20]
    print(f"Original: {list3}, Reversed: {ListReverser.reverse(list3)}")