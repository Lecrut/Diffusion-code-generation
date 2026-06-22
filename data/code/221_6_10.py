class ValueSorter:
    def sort_three(self, a, b, c):
        min_val = min(a, b, c)
        max_val = max(a, b, c)
        middle_val = a + b + c - min_val - max_val
        return (min_val, middle_val, max_val)

if __name__ == '__main__':
    sorter = ValueSorter()
    x = 5
    y = 2
    z = 8
    result = sorter.sort_three(x, y, z)
    print(result)