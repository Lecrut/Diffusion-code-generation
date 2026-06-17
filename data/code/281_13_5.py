class ValueSummer:
    def __init__(self):
        pass
    def calculate_sum(self, *args):
        return sum(args)
if __name__ == '__main__':
    summer = ValueSummer()
    numbers1 = 1, 5, 10
    result1 = summer.calculate_sum(*numbers1)
    print(f"Sum of {numbers1}: {result1}")
    numbers2 = 2.5, 3.5, 1.0
    result2 = summer.calculate_sum(*numbers2)
    print(f"Sum of {numbers2}: {result2}")
    numbers3 = 100
    result3 = summer.calculate_sum(numbers3)
    print(f"Sum of {numbers3}: {result3}")
    numbers4 = 7, 2, 8, 3
    result4 = summer.calculate_sum(*numbers4)
    print(f"Sum of {numbers4}: {result4}")