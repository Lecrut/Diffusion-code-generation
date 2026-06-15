class NumberSorter:
    def sort_three(self, a, b, c):
        try:
            num1 = float(a)
            num2 = float(b)
            num3 = float(c)
            sorted_list = sorted([num1, num2, num3])
            return sorted_list
        except ValueError:
            raise ValueError("All inputs must be numeric.")
if __name__ == '__main__':
    sorter = NumberSorter()
    print(f"Sorting (1, 5, 3): {sorter.sort_three(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sorter.sort_three(10, -2, 7)}")
    try:
        print(f"Sorting ('a', 5, 3): {sorter.sort_three('a', 5, 3)}")
    except ValueError as e:
        print(f"Error caught: {e}")
    try:
        print(f"Sorting (1, 'b', 3): {sorter.sort_three(1, 'b', 3)}")
    except ValueError as e:
        print(f"Error caught: {e}")