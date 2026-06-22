class IntegerComparer:
    def __init__(self, first_value, second_value):
        self.first_value = first_value
        self.second_value = second_value

    def compare(self):
        return self.first_value > self.second_value

if __name__ == '__main__':
    comparer1 = IntegerComparer(25, 10)
    print(comparer1.compare())

    comparer2 = IntegerComparer(5, 30)
    print(comparer2.compare())