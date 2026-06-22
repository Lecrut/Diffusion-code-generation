class ComparisonTool:
    _LARGE_NUMBER_THRESHOLD = 10**9

    @staticmethod
    def is_large_number(value):
        return abs(value) > ComparisonTool._LARGE_NUMBER_THRESHOLD

    def check_greater(self, value1, value2):
        if self.is_large_number(value1) or self.is_large_number(value2):
            return self.compare_large_numbers(value1, value2)
        else:
            return value1 > value2

    @staticmethod
    def compare_large_numbers(num1, num2):
        str_num1 = str(num1)
        str_num2 = str(num2)
        
        if len(str_num1) != len(str_num2):
            return len(str_num1) > len(str_num2)
        
        return int(str_num1) > int(str_num2)

if __name__ == '__main__':
    tool = ComparisonTool()
    result = tool.check_greater(10**1000, 999**999)
    print(result)