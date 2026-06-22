class NumberSorter:

    @staticmethod
    def sort_three_numbers(a, b, c):
        if a <= b and a <= c:
            first = a
            if b <= c:
                second, third = (b, c)
            else:
                second, third = (c, b)
        elif b <= a and b <= c:
            first = b
            if a <= c:
                second, third = (a, c)
            else:
                second, third = (c, a)
        else:
            first = c
            if a <= b:
                second, third = (a, b)
            else:
                second, third = (b, a)
        return (first, second, third)
if __name__ == '__main__':
    sorter = NumberSorter()
    result1 = sorter.sort_three_numbers(5, 2, 8)
    print(result1)
    result2 = sorter.sort_three_numbers(100, 1, 50)
    print(result2)
    result3 = sorter.sort_three_numbers(3, 3, 3)
    print(result3)