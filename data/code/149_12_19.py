class ListReverser:
    def __init__(self, input_list):
        self.input_list = input_list

    def reverse(self):
        return list(reversed(self.input_list))

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    reverser = ListReverser(sample_input)
    reversed_list = reverser.reverse()
    print(reversed_list)