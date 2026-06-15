class NumberSorter:
    def sort_three(self, a, b, c):
        numbers = sorted([a, b, c])
        return numbers
if __name__ == '__main__':
    sorter = NumberSorter()
    result1 = sorter.sort_three(5, 2, 8)
    print(f"Sorted (5, 2, 8): {result1}")
    result2 = sorter.sort_three(100, -5, 30)
    print(f"Sorted (100, -5, 30): {result2}")
    result3 = sorter.sort_three(-1, -10, -5)
    print(f"Sorted (-1, -10, -5): {result3}")