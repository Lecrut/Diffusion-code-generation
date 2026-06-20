class Comparator:
    def compare(self, x, y):
        if type(x) != type(y):
            return f"Type mismatch: Cannot directly compare {type(x)} and {type(y)}"
        
        if isinstance(x, int):
            if x < y:
                return f"Comparison: {x} < {y}"
            elif x > y:
                return f"Comparison: {x} > {y}"
            else:
                return f"Comparison: {x} == {y}"
        
        if isinstance(x, str):
            if x < y:
                return f"Comparison: '{x}' < '{y}'"
            elif x > y:
                return f"Comparison: '{x}' > '{y}'"
            else:
                return f"Comparison: '{x}' == '{y}'"

if __name__ == '__main__':
    comparator = Comparator()
    print("--- Integer Comparison ---")
    print(comparator.compare(10, 5))
    print(comparator.compare(20, 20))
    print(comparator.compare(3, 1))
    
    print("--- String Comparison ---")
    print(comparator.compare("apple", "banana"))
    print(comparator.compare("cherry", "cherry"))
    print(comparator.compare("date", "apple"))