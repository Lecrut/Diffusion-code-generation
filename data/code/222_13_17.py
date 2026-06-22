class LexicographicalMinFinder:
    def __init__(self):
        self.minimum = None

    def update_minimum(self, value):
        if self.minimum is None or value < self.minimum:
            self.minimum = value

    def get_minimum(self):
        return self.minimum

if __name__ == '__main__':
    finder = LexicographicalMinFinder()
    sample_input = "apple banana cherry"
    for item in sample_input.split():
        finder.update_minimum(item)
    print(finder.get_minimum())