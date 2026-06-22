class NumberSorter:
    def sort(self, a, b, c):
        if a <= b and a <= c:
            smallest = a
            if b <= c:
                middle = b
                largest = c
            else:
                middle = c
                largest = b
        elif b <= a and b <= c:
            smallest = b
            if a <= c:
                middle = a
                largest = c
            else:
                middle = c
                largest = a
        else:
            smallest = c
            if a <= b:
                middle = a
                largest = b
            else:
                middle = b
                largest = a
        return smallest, middle, largest

if __name__ == '__main__':
    sorter = NumberSorter()
    result1 = sorter.sort(5, 2, 8)
    print(result1)
    result2 = sorter.sort(100, 1, 50)
    print(result2)
    result3 = sorter.sort(3, 3, 3)
    print(result3)