class ListReverser:
    def reverse_list(self, data):
        return [data[i] for i in range(len(data)-1, -1, -1)]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse_list(sample_list)
    print(reversed_list)