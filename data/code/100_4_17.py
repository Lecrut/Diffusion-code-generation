class GreaterChecker:
    @staticmethod
    def is_greater(x, y):
        return x > y

if __name__ == '__main__':
    sample_x = 5
    sample_y = 3
    result = GreaterChecker.is_greater(sample_x, sample_y)
    print(f"Is {sample_x} greater than {sample_y}? {result}")