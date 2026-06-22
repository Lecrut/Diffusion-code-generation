class ComparisonTool:

    def check_greater(self, value1, value2):
        try:
            return value1 > value2
        except TypeError:
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('a', 'b'))
    print(tool.check_greater([1, 2], [1]))
    print(tool.check_greater({'key': 'value'}, {'another_key': 'another_value'}))