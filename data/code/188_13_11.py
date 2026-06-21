class ListReverser:
    def reverse(self, iterable):
        return list(iterable[::-1])

if __name__ == '__main__':
    reverser = ListReverser()
    sample1 = [1, 2, 3, 4, 5]
    print(f"Original: {sample1}, Reversed: {reverser.reverse(sample1)}")
    sample2 = ['a', 'b', 'c']
    print(f"Original: {sample2}, Reversed: {reverser.reverse(sample2)}")
    empty_list = []
    print(f"Original: {empty_list}, Reversed: {reverser.reverse(empty_list)}")
    single_element = [10]
    print(f"Original: {single_element}, Reversed: {reverser.reverse(single_element)}")