class ValueSummer:
    def __init__(self):
        pass
    def calculate_sum(self, *args):
        total = 0
        for num in args:
            total += num
        return total
if __name__ == '__main__':
    summer = ValueSummer()
    numbers1 = (1, 2, 3, 4, 5)
    result1 = summer.calculate_sum(*numbers1)
    print(f"Sum of {list(numbers1)} is: {result1}")
    numbers2 = (10, 20, 30)
    result2 = summer.calculate_sum(10, 20, 30)
    print(f"Sum of {list(numbers2)} is: {result2}")
    numbers3 = (5, 5, 10, 15)
    result3 = summer.calculate_sum(*numbers3)
    print(f"Sum of {list(numbers3)} is: {result3}")