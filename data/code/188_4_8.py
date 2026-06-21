import functools

class ListReverser:
    @staticmethod
    def reverse_with_reduce(lst):
        return functools.reduce(lambda acc, x: [x] + acc, lst, [])

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse_with_reduce(sample_list)
    print(reversed_list)

    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverser.reverse_with_reduce(sample_list_2)
    print(reversed_list_2)

    sample_list_3 = [10, 20, 30]
    reversed_list_3 = reverser.reverse_with_reduce(sample_list_3)
    print(reversed_list_3)