class MaxFinder:
    def __init__(self, values):
        if len(values) != 3:
            raise ValueError("Exactly three values are required.")
        self.values = values

    def get_maximum(self):
        return max(*self.values)

if __name__ == '__main__':
    sample_values = [42, 17, 99]
    finder = MaxFinder(sample_values)
    print(finder.get_maximum())