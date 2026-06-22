class MinMaxFinder:
    @staticmethod
    def find_min_max(values):
        if not values:
            return None, None
        
        smallest = largest = values[0]
        
        for value in values[1:]:
            if value < smallest:
                smallest = value
            elif value > largest:
                largest = value
        
        return smallest, largest

if __name__ == '__main__':
    sample_values = (34, -56, 78, 21, -9, 0)
    min_val, max_val = MinMaxFinder.find_min_max(sample_values)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")