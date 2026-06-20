class BooleanComparator:
    def compare(self, a: bool, b: bool) -> bool:
        return a == b

if __name__ == '__main__':
    comparator = BooleanComparator()
    print(f"Comparing True and True: {comparator.compare(True, True)}")
    print(f"Comparing False and False: {comparator.compare(False, False)}")
    print(f"Comparing True and False: {comparator.compare(True, False)}")
    print(f"Comparing False and True: {comparator.compare(False, True)}")