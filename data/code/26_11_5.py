class ComparisonTool:
    def check_greater(self, a, b):
        try:
            return a > b
        except TypeError:
            return False
if __name__ == '__main__':
    tool = ComparisonTool()
    print(f"10 > 5: {tool.check_greater(10, 5)}")
    print(f"-3 > 0: {tool.check_greater(-3, 0)}")
    print(f"5 > 5: {tool.check_greater(5, 5)}")
    print(f"10.5 > 10: {tool.check_greater(10.5, 10)}")
    print(f"'a' > 10: {tool.check_greater('a', 10)}")
    print(f"None > 5: {tool.check_greater(None, 5)}")