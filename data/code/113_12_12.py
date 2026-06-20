class FloatDifference:
    @staticmethod
    def compute_diff(a, b):
        return a - b

if __name__ == '__main__':
    result = FloatDifference.compute_diff(10.5, 4.2)
    print(result)