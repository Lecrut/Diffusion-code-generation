def string_to_number(s):
    try:
        return int(s)
    except ValueError:
        raise TypeError("Invalid input")

class NumberFinder:
    MAX_VALUE = float('-inf')

    @staticmethod
    def find_largest(numbers):
        if not numbers:
            return None
        
        max_val = NumberFinder.MAX_VALUE
        
        for number in numbers:
            numeric_value = string_to_number(number)
            if numeric_value > max_val:
                max_val = numeric_value
        
        return max_val

if __name__ == '__main__':
    data1 = ['10', '5', '20', '8', '30']
    print("Max of data1:", NumberFinder.find_largest(data1))
    data2 = ['-5', '-1', '-10', '-2']
    print("Max of data2:", NumberFinder.find_largest(data2))
    data3 = ['42']
    print("Max of data3:", NumberFinder.find_largest(data3))
    data4 = []
    print("Max of data4:", NumberFinder.find_largest(data4))