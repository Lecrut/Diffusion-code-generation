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
    sum1 = summer.calculate_sum(*numbers1)
    print(f"Sum of {list(numbers1)} is: {sum1}")
    numbers2 = (10, 20, 30)
    sum2 = summer.calculate_sum(*numbers2)
    print(f"Sum of {list(numbers2)} is: {sum2}")
    numbers3 = (5, 5, 5, 5)
    sum3 = summer.calculate_sum(*numbers3)
    print(f"Sum of {list(numbers3)} is: {sum3}")
    numbers4 = ()
    sum4 = summer.calculate_sum(*numbers4)
    print(f"Sum of an empty set is: {sum4}")