class ValueSummer:
    def sum_all(self, *args):
        total = 0
        for num in args:
            total += num
        return total
if __name__ == '__main__':
    summer = ValueSummer()
    result1 = summer.sum_all(1, 2, 3)
    print(f"Sum of (1, 2, 3): {result1}")
    result2 = summer.sum_all(10, 20, 30, 40)
    print(f"Sum of (10, 20, 30, 40): {result2}")
    result3 = summer.sum_all(5)
    print(f"Sum of (5): {result3}")
    result4 = summer.sum_all()
    print(f"Sum of (): {result4}")