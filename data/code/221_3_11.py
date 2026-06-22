class NumberSorter:
    def sort_three(self, a, b, c):
        return sorted([a, b, c])

if __name__ == '__main__':
    sorter = NumberSorter()
    result1 = sorter.sort_three(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sorter.sort_three(100, -5, 33)
    print(f"Sorted (100, -5, 33): {result2}")
    result3 = sorter.sort_three(-1, -50, 0)
    print(f"Sorted (-1, -50, 0): {result3}")