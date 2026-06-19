class ComparisonTool:
    def check_greater(self, value1, value2):
        try:
            return float(value1) > float(value2)
        except ValueError:
            raise TypeError("Both values must be convertible to float")

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10, 5)
    print(result)