class ComparisonTool:
    def __init__(self):
        self.result = None

    def check_greater(self, a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise ValueError("Both inputs must be integers or floats.")
        self.result = a > b
        return self.result

if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater(5, 10))
    print(tool.check_greater(7.5, 7.5))
    print(tool.check_greater(200, 199))
    try:
        print(tool.check_greater("a", 10))
    except ValueError as e:
        print(e)