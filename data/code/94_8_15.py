class TruthInspector:
    def __init__(self, sequence):
        self.sequence = sequence

    def contains_truth(self):
        if not self.sequence:
            return False
        for element in self.sequence:
            if element is True:
                return True
        return False

    def is_all_false(self):
        return not self.contains_truth()

if __name__ == '__main__':
    test_data = [False, False, False]
    inspector = TruthInspector(test_data)
    print(inspector.contains_truth())
    print(inspector.is_all_false())