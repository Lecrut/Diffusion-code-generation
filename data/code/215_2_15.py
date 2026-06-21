class MaxFinder:
    @staticmethod
    def find_max(values):
        max_value = values[0]
        for value in values:
            if value > max_value:
                max_value = value
        return max_value

if __name__ == '__main__':
    sample_values = [100, 200, 50, 300, 75]
    max_value = MaxFinder.find_max(sample_values)
    print(max_value)