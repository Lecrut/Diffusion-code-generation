class MaxFinder:
    def find_max(self, data):
        if not data:
            raise ValueError("Input dictionary cannot be empty")
        return max(data.values())

if __name__ == '__main__':
    finder = MaxFinder()
    dict1 = {'a': 1, 'b': 5, 'c': 2, 'd': 9, 'e': 3}
    dict2 = {'x': -10, 'y': -5, 'z': -1}
    dict3 = {}
    
    try:
        result1 = finder.find_max(dict1)
        print(f"Max of {dict1}: {result1}")
        result2 = finder.find_max(dict2)
        print(f"Max of {dict2}: {result2}")
        finder.find_max(dict3)
    except ValueError as e:
        print(f"Error caught: {e}")