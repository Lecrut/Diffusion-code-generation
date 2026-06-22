class NumberSorter:
    def sort_three(self, a, b, c):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float))):
            raise TypeError("All inputs must be numbers.")
        
        if a > b:
            a, b = b, a
        if b > c:
            b, c = c, b
        if a > b:
            a, b = b, a
        
        return [a, b, c]

if __name__ == '__main__':
    sorter = NumberSorter()
    print(f"Sorting (1, 5, 3): {sorter.sort_three(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sorter.sort_three(10, -2, 7)}")
    try:
        print(f"Sorting ('a', 5, 3): {sorter.sort_three('a', 5, 3)}")
    except TypeError as e:
        print(f"Error caught: {e}")