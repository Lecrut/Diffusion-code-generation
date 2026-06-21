class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse(self):
        return self.input_list[::-1]

if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    reverser = ListReverser(sample_list)
    reversed_list = reverser.reverse()
    print(reversed_list)

    another_list = ['a', 'b', 'c', 'd', 'e']
    another_reverser = ListReverser(another_list)
    another_reversed_list = another_reverser.reverse()
    print(another_reversed_list)