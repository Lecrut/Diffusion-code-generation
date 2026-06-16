class ListReverser:
    def reverse_list(self, data_list):
        return data_list[::-1]
if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5]
    reverser = ListReverser()
    reversed_list = reverser.reverse_list(my_list)
    print(reversed_list)