class BooleanComparator:

    def __init__(self, value: bool):
        self.value = value

    def compare(self, other: 'BooleanComparator') -> bool:
        return self.value == other.value
if __name__ == '__main__':
    comp1_true = BooleanComparator(True)
    comp2_false = BooleanComparator(False)
    comp3_true = BooleanComparator(True)
    print(comp1_true.compare(comp2_false))
    print(comp3_true.compare(comp2_false))
    print(comp1_true.compare(comp3_true))