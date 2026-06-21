class ListReverser:
    def __init__(self, data):
        self.data = data

    def reverse(self):
        return list(reversed(self.data))

if __name__ == '__main__':
    sample_input = [10, 20, 30, 40, 50]
    reverser = ListReverser(sample_input)
    reversed_list = reverser.reverse()
    print(reversed_list)