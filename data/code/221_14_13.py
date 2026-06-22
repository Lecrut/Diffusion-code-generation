class NumberSorter:
    @staticmethod
    def sort_numbers(a, b, c):
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        return a, b, c

if __name__ == '__main__':
    num1, num2, num3 = NumberSorter.sort_numbers(5, 2, 8)
    print(f"Sorted numbers: {num1}, {num2}, {num3}")
    num1, num2, num3 = NumberSorter.sort_numbers(100, 42, 34)
    print(f"Sorted numbers: {num1}, {num2}, {num3}")
    num1, num2, num3 = NumberSorter.sort_numbers(7, 7, 7)
    print(f"Sorted numbers: {num1}, {num2}, {num3}")