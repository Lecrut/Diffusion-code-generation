class SetOverlapChecker:
    def check_overlap(self, set1, set2, set3):
        return not (set1.isdisjoint(set2) and set1.isdisjoint(set3) and set2.isdisjoint(set3))

if __name__ == '__main__':
    checker = SetOverlapChecker()
    sets1 = {1, 2}, {3, 4}, {5, 6}
    print(f"Sets 1: {sets1}, Overlap: {checker.check_overlap(*sets1)}")
    sets2 = {1, 2, 3}, {4, 5, 6}, {7, 8, 9}
    print(f"Sets 2: {sets2}, Overlap: {checker.check_overlap(*sets2)}")