class NumberSorter:
    def sort_three(self, a, b, c):
        if not all(isinstance(x, (int, float)) for x in [a, b, c]):
            raise ValueError("All inputs must be numbers.")
        
        if a > b:
            a, b = b, a
        if a > c:
            a, c = c, a
        if b > c:
            b, c = c, b
        
        return [a, b, c]

if __name__ == '__main__':
    sorter = NumberSorter()
    print(f"Sorting (1, 5, 3): {sorter.sort_three(1, 5, 3)}")
    print(f"Sorting (10, -2, 7): {sorter.sort_three(10, -2, 7)}")
    try:
        print(f"Sorting ('a', 5, 3): {sorter.sort_three('a', 5, 3)}")
    except ValueError as e:
        print(f"Error caught: {e}")