class SecondSmallestFinder:
    @staticmethod
    def find_second_smallest(data):
        if len(data) < 2:
            raise ValueError("Input list must contain at least two elements")
        
        first, second = float('inf'), float('inf')
        
        for num in data:
            if num <= first:
                first, second = num, first
            elif num < second:
                second = num
        
        return second

if __name__ == '__main__':
    sample_list = [45, 12, 89, 3, 56, 7]
    try:
        second_smallest_value = SecondSmallestFinder.find_second_smallest(sample_list)
        print(second_smallest_value)
    except ValueError as e:
        print(f"Error: {e}")