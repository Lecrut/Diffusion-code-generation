class ValueDiffer:
    def calculate_difference(self, val1, val2):
        return val1 - val2
if __name__ == '__main__':
    differ = ValueDiffer()
    a = 100
    b = 45
    result = differ.calculate_difference(a, b)
    print(result)