class BoolListInverter:
    def __init__(self, bool_list):
        self.bool_list = bool_list

    def invert(self):
        return [not x for x in self.bool_list]

if __name__ == '__main__':
    sample_values = [True, False, True, False]
    inverter = BoolListInverter(sample_values)
    inverted_values = inverter.invert()
    print(inverted_values)