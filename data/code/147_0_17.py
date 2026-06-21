class Sorter:
    def __init__(self, numbers):
        self.numbers = numbers

    def sort_ascending(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter_instance = Sorter([34, 7, 23, 32, 5, 62])
    sorted_list = sorter_instance.sort_ascending()
    print(sorted_list)