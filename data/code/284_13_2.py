class DataReverser:
    def __init__(self):
        self.data = []
    def reverse_data(self):
        self.data.reverse()
if __name__ == '__main__':
    reverser = DataReverser()
    reverser.data = [1, 2, 3, 4, 5]
    print("Original data:", reverser.data)
    reverser.reverse_data()
    print("Reversed data:", reverser.data)