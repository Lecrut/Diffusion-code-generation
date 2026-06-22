class MathUtility:
    @staticmethod
    def is_negative(number):
        return number < 0

if __name__ == '__main__':
    sample_values = [-1, 2, -3.5, 4, 0]
    utility_instance = MathUtility()
    
    for value in sample_values:
        print(f"{value} is negative: {utility_instance.is_negative(value)}")