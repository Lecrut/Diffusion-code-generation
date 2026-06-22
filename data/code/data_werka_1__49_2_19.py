class LengthComparer:
    def __init__(self, length1, length2):
        self.length1 = float(length1)
        self.length2 = float(length2)

    def compare(self):
        if self.length1 > self.length2:
            return "Length 1 is greater than Length 2"
        elif self.length1 < self.length2:
            return "Length 1 is less than Length 2"
        else:
            return "Length 1 is equal to Length 2"

if __name__ == '__main__':
    lengths = {
        'length1': '5.7',
        'length2': '3.2'
    }
    comparer = LengthComparer(lengths['length1'], lengths['length2'])
    print(comparer.compare())