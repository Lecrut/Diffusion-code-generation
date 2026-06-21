class Sorter:
    def __init__(self, data):
        self.data = data

    def sort_data(self):
        return sorted(self.data)

if __name__ == '__main__':
    sorter = Sorter([5, 2, 8, 1, 9, 3])
    sorted_numbers = sorter.sort_data()
    print(sorted_numbers)