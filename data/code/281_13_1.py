class ValueSummer:
    def __init__(self):
        pass
    def calculate_sum(self, *args):
        return sum(args)
if __name__ == '__main__':
    summer = ValueSummer()
    result1 = summer.calculate_sum(1, 2, 3)
    print(f"Sum of (1, 2, 3): {result1}")
    result2 = summer.calculate_sum(10, 20, 30, 40)
    print(f"Sum of (10, 20, 30, 40): {result2}")
    result3 = summer.calculate_sum(5)
    print(f"Sum of (5): {result3}")
    result4 = summer.calculate_sum()
    print(f"Sum of (): {result4}")