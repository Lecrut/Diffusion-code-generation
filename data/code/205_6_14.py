class Quicksort:
    def sort(self, items):
        if len(items) <= 1:
            return items
        pivot = items[len(items) // 2]
        left = [x for x in items if x < pivot]
        middle = [x for x in items if x == pivot]
        right = [x for x in items if x > pivot]
        return self.sort(left) + middle + self.sort(right)

if __name__ == '__main__':
    sorter = Quicksort()
    data = [5, 2, 8, 1, 9]
    sorted_data = sorter.sort(data)
    print(sorted_data)