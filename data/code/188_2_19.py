class ListReverser:
    def reverse_using_iter(self, lst):
        return list(reversed(lst))

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse_using_iter(sample_list)
    print(reversed_list)