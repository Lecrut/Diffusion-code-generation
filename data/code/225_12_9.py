class MinMaxFinder:
    def find_min_max(self, data):
        min_val = None
        max_val = None
        min_key = None
        max_key = None
        
        for key, value in data.items():
            if min_val is None or value < min_val:
                min_val = value
                min_key = key
            if max_val is None or value > max_val:
                max_val = value
                max_key = key
        
        return (min_key, min_val), (max_key, max_val)

if __name__ == '__main__':
    finder = MinMaxFinder()
    data_dict = {'a': 10, 'b': 5, 'c': 20, 'd': 15}
    min_result, max_result = finder.find_min_max(data_dict)
    print(f"Min: {min_result}, Max: {max_result}")