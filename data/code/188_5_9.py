class ListReverser:
    @staticmethod
    def reverse_recursive(lst):
        if len(lst) <= 1:
            return lst
        else:
            return [lst[-1]] + ListReverser.reverse_recursive(lst[:-1])

if __name__ == '__main__':
    print(ListReverser.reverse_recursive([1, 2, 3, 4, 5]))
    print(ListReverser.reverse_recursive(['a', 'b', 'c']))
    print(ListReverser.reverse_recursive([]))
    print(ListReverser.reverse_recursive([7]))