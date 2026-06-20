class NumberDifference:
    def __init__(self, a, b):
        if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
            raise ValueError("Both inputs must be numbers.")
        self.a = a
        self.b = b
    
    def compute_difference(self):
        return abs(self.a - self.b)

if __name__ == '__main__':
    diff_instance = NumberDifference(10, 5)
    print(diff_instance.compute_difference())