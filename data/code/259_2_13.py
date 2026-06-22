class MinMaxFinder:
    @staticmethod
    def compare(a, b):
        if a < b:
            return -1
        elif a > b:
            return 1
        else:
            return 0

    @staticmethod
    def get_min_max(data_tuple):
        if not data_tuple:
            return None, None
        
        minimum = data_tuple[0]
        maximum = data_tuple[0]
        
        for item in data_tuple:
            if MinMaxFinder.compare(item, minimum) < 0:
                minimum = item
            if MinMaxFinder.compare(item, maximum) > 0:
                maximum = item
                
        return minimum, maximum

if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data1 = (10, 5, 20, 8, 15)
    min1, max1 = finder.get_min_max(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Minimum: {min1}, Maximum: {max1}")