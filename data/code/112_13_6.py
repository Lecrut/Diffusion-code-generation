class SummationTool:
    def __init__(self, value1: int, value2: int):
        self.value1 = value1
        self.value2 = value2
    
    def calculate_sum(self) -> int:
        return self.value1 + self.value2

if __name__ == '__main__':
    tool = SummationTool(7, 3)
    sum_result = tool.calculate_sum()
    print(sum_result)