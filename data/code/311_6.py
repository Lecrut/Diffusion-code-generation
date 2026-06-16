class ListReverser:
    def get_reversed_elements(self, data):
        return data[::-1]
if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.get_reversed_elements(sample_list)
    print(reversed_list)
    sample_list_2 = ['a', 'b', 'c', 'd']
    reversed_list_2 = reverser.get_reversed_elements(sample_list_2)
    print(reversed_list_2)