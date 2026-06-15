class NumberSorter:
    def sort_three(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers
if __name__ == '__main__':
    sorter = NumberSorter()
    result1 = sorter.sort_three(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sorter.sort_three(-10, 0, 3)
    print(f"Sorted (-10, 0, 3): {result2}")
    result3 = sorter.sort_three(7, 7, 7)
    print(f"Sorted (7, 7, 7): {result3}")