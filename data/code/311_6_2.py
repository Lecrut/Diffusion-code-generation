class ListReverser:
    def get_reversed_elements(self, data):
        reversed_list = data[::-1]
        return reversed_list
if __name__ == '__main__':
    reverser = ListReverser()
    sample_data = [1, 2, 3, 4, 5]
    reversed_result = reverser.get_reversed_elements(sample_data)
    print(reversed_result)