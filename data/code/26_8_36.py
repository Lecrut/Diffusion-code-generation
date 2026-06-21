class ComparisonTool:
    def __init__(self):
        self.comparable_types = {
            int: True,
            float: True,
            str: True,
            list: True,
            tuple: True,
            dict: True,
            set: True
        }

    def is_comparable(self, value):
        return type(value) in self.comparable_types

    def check_greater(self, value1, value2):
        if not (self.is_comparable(value1) and self.is_comparable(value2)):
            raise ValueError('Both values must be comparable types')
        try:
            return value1 > value2
        except TypeError:
            raise ValueError('Failed to compare the values')

if __name__ == '__main__':
    tool = ComparisonTool()
    print(tool.check_greater(10, 5))
    print(tool.check_greater('b', 'a'))
    print(tool.check_greater([2, 3], [1]))
    try:
        print(tool.check_greater('10', 5))
    except ValueError as e:
        print(e)