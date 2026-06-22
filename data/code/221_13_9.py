class Sorter:
    def __init__(self, a, b, c):
        self.numbers = [a, b, c]

    def sort_numbers(self):
        return sorted(self.numbers)

if __name__ == '__main__':
    sorter_instance = Sorter(3, 1, 2)
    sorted_sequence = sorter_instance.sort_numbers()
    print(sorted_sequence)