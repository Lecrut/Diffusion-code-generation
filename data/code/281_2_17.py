class ValueSummer:
    def __init__(self, values):
        self.values = values

    @staticmethod
    def sum_values(values):
        total = 0
        for value in values:
            total += value
        return total

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45]
    summer = ValueSummer(sample_list)
    result = summer.sum_values()
    print(result)