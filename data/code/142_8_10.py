class BooleanComparator:
    @staticmethod
    def compare(bool1, bool2):
        return bool1 == bool2

if __name__ == '__main__':
    sample1 = True
    sample2 = False
    result = BooleanComparator.compare(sample1, sample2)
    print(result)