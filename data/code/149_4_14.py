class ListReverser:
    def reverse(self, input_list):
        return [input_list[i] for i in range(len(input_list)-1, -1, -1)]

if __name__ == '__main__':
    reverser = ListReverser()
    sample_list = [1, 2, 3, 4, 5]
    reversed_list = reverser.reverse(sample_list)
    print(reversed_list)