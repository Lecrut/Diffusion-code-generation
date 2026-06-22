class LengthComparator:
    def __init__(self, len1, len2):
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
    comparator = LengthComparator(50, 25)
    print(comparator.compare())
    
    another_comparator = LengthComparator(30, 30)
    print(another_comparator.compare())
    
    yet_another_comparator = LengthComparator(10, 40)
    print(yet_another_comparator.compare())