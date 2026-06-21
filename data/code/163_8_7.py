class FruitSorter:
    def __init__(self):
        self.fruits = []

    def add_fruit(self, fruit, color):
        self.fruits.append((fruit, color))

    def sort_by_color(self):
        return sorted(self.fruits, key=lambda x: x[1])

if __name__ == '__main__':
    sorter = FruitSorter()
    sorter.add_fruit("apple", "red")
    sorter.add_fruit("banana", "yellow")
    sorter.add_fruit("grape", "purple")
    sorted_fruits = sorter.sort_by_color()
    print(sorted_fruits)