class ListReverser:
    def reverse_list(self, lst):
        return lst[::-1]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_data = [1, 2, 3, 4, 5]
    reversed_data = reverser.reverse_list(sample_data)
    print(reversed_data)