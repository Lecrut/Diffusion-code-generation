class EmptySequenceException(Exception):
    def __init__(self, message="Data sequence cannot be empty"):
        super().__init__(message)

def find_peak_value(points):
    if not isinstance(points, tuple):
        raise TypeError("Input must be a tuple")
    if len(points) == 0:
        raise EmptySequenceException()
    
    highest = None
    
    for item in points:
        if isinstance(item, bool):
            raise TypeError("Boolean values are not allowed")
        if not isinstance(item, (int, float)):
            raise TypeError("All data points must be numeric")
        
        numeric_item = float(item)
        
        if highest is None:
            highest = numeric_item
        else:
            if numeric_item > highest:
                highest = numeric_item
                
    return highest

if __name__ == '__main__':
    test_tuple = (42.5, 17.1, 99.9, -5.5, 0.0)
    peak_result = find_peak_value(test_tuple)
    print(peak_result)