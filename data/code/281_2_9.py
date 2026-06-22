class ValueSummer:
    def __init__(self, values):
        self.values = values
    
    def sum_values(self):
        total = 0
        for value in self.values:
            total += value
        return total

if __name__ == '__main__':
    sample_list = [10, 25, 30, 45]
    summer = ValueSummer(sample_list)
    result = summer.sum_values()
    print(result)