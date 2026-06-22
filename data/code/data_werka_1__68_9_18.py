class MathOperations:
    @staticmethod
    def absolute_difference(num1, num2):
        return abs(num1 - num2)

def find_difference(num1, num2):
    return MathOperations.absolute_difference(num1, num2)

if __name__ == '__main__':
    value1 = 15
    value2 = 8
    print(find_difference(value1, value2))
    
    value3 = 27
    value4 = 30
    print(find_difference(value3, value4))
    
    value5 = -5
    value6 = -10
    print(find_difference(value5, value6))