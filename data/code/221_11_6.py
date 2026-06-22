class NumberSorter:
    @staticmethod
    def sort_three_numbers(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return (a, b, c)

if __name__ == '__main__':
    sorter = NumberSorter()
    result = sorter.sort_three_numbers(3, 1, 2)
    print(result)