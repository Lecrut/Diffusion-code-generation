class RangeCalculator:
    @staticmethod
    def find_min_max(data):
        if not data:
            raise ValueError("Data list cannot be empty")
        minimum = data[0]
        maximum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return minimum, maximum

if __name__ == '__main__':
    calculator = RangeCalculator()
    list1 = [5.5, 2.3, 9.8, 1.2, 7.4]
    min_val, max_val = calculator.find_min_max(list1)
    print(f"Min: {min_val}, Max: {max_val}")
    
    list2 = [-10.5, 5.6, 0.0, -3.2, 8.9]
    min_val, max_val = calculator.find_min_max(list2)
    print(f"Min: {min_val}, Max: {max_val}")
    
    list3 = [42.7]
    min_val, max_val = calculator.find_min_max(list3)
    print(f"Min: {min_val}, Max: {max_val}")