class FruitSorter:
    @staticmethod
    def sort_by_color(fruits):
        return sorted(fruits, key=lambda x: x[1])

if __name__ == '__main__':
    fruits = [("apple", "red"), ("banana", "yellow"), ("grape", "purple")]
    sorted_fruits = FruitSorter.sort_by_color(fruits)
    print(sorted_fruits)