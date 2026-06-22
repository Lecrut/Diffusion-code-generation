class MinMaxFinder:
    MIN_VALUE = float('-inf')
    MAX_VALUE = float('inf')

    @staticmethod
    def find_min_max(data):
        if not data:
            raise ValueError("Input list cannot be empty")
        
        smallest = MinMaxFinder.MIN_VALUE
        largest = MinMaxFinder.MAX_VALUE
        
        for x in data:
            if x < smallest:
                smallest = x
            if x > largest:
                largest = x
        
        return smallest, largest

if __name__ == '__main__':
    sample_list = [34, 12, 56, 89, 3, 72]
    min_val, max_val = MinMaxFinder.find_min_max(sample_list)
    print(f"Smallest value: {min_val}")
    print(f"Largest value: {max_val}")