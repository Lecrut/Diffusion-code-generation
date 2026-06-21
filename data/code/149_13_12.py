class ListReverser:
    def __init__(self, data):
        self.data = data

    def reverse(self):
        return self.data[::-1]

if __name__ == '__main__':
    reverser = ListReverser([1, 2, 3, 4, 5])
    print(reverser.reverse())