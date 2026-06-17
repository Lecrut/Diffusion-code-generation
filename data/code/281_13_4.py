class ValueSummer:
    def __init__(self):
        pass
    def sum_all(self, *args):
        total = 0
        for num in args:
            total += num
        return total
if __name__ == '__main__':
    summer = ValueSummer()
    numbers1 = 1, 5, 10
    result1 = summer.sum_all(*numbers1)
    print(f"Sum of {numbers1}: {result1}")
    numbers2 = 2.5, 3.5, 1.0
    result2 = summer.sum_all(*numbers2)
    print(f"Sum of {numbers2}: {result2}")
    numbers3 = 100, 200, -50
    result3 = summer.sum_all(*numbers3)
    print(f"Sum of {numbers3}: {result3}")