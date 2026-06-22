class ComparisonTool:

    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_greater(self):
        return self.value1 > self.value2
if __name__ == '__main__':
    tool = ComparisonTool(10, 5)
    print(tool.check_greater())
    tool = ComparisonTool(3, 8)
    print(tool.check_greater())