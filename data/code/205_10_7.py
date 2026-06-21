class Sorter:
    def __init__(self, data):
        self.data = data

    def sort_data(self):
        return sorted(self.data)

if __name__ == '__main__':
    sorter_instance = Sorter([5, 2, 8, 1, 9, 3])
    sorted_numbers = sorter_instance.sort_data()
    print(sorted_numbers)