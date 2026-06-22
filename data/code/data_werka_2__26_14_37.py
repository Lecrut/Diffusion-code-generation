class IntegerComparison:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def check_greater(self):
        return self.value1 > self.value2

    def check_less(self):
        return self.value1 < self.value2

if __name__ == '__main__':
    sample_value1 = 20
    sample_value2 = 8
    comparison = IntegerComparison(sample_value1, sample_value2)
    
    print("Is value1 greater than value2?", comparison.check_greater())
    print("Is value1 less than value2?", comparison.check_less())