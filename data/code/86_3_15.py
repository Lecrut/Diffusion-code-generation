class BooleanComparer:
    def compare(self, b1, b2):
        return [b1 == b2]

if __name__ == '__main__':
    comparer = BooleanComparer()
    print(comparer.compare(True, False))
    print(comparer.compare(True, True))
    print(comparer.compare(False, True))