class LengthComparator:
    def __init__(self, len1, len2):
        if not isinstance(len1, (int, float)) or not isinstance(len2, (int, float)):
            raise ValueError("Both inputs must be numbers")
        self.len1 = len1
        self.len2 = len2

    def compare(self):
        if self.len1 == self.len2:
            return 'equal'
        elif self.len1 > self.len2:
            return 'len1 is greater'
        else:
            return 'len2 is smaller'

if __name__ == '__main__':
    try:
        length_comparator = LengthComparator(10, 5)
        result = length_comparator.compare()
        print(result)
    except ValueError as e:
        print(e)