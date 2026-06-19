import math

def compare_values(value1: float, value2: float) -> bool:
    if math.isclose(value1, value2):
        return False
    return value1 > value2
if __name__ == '__main__':
    sample_value1 = 3.141592653589793
    sample_value2 = 3.141592653589792
    result = compare_values(sample_value1, sample_value2)
    print(result)