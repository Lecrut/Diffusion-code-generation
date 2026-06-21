class ListReverser:
    def reverse_list(self, lst):
        return lst[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_values = [[], [1], [1, 2, 3, 4]]
    for values in sample_values:
        print(reverser.reverse_list(values))