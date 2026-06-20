class FloatDifference:
    A = 10.5
    B = 4.2
    
    @staticmethod
    def calculate_difference(a=A, b=B):
        return a - b

if __name__ == '__main__':
    result = FloatDifference.calculate_difference()
    print(result)