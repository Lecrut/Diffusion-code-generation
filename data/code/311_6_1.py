class ListReverser:
    def get_reversed_elements(self, data):
        return data[::-1]
if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.get_reversed_elements(sample_list)
    print(reversed_list)