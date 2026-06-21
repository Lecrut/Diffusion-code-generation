class ContradictionChecker:

    def check(self, statements):
        n = len(statements)
        for i in range(n):
            for j in range(i + 1, n):
                s1 = statements[i]
                s2 = statements[j]
                if self._are_contradictory(s1, s2):
                    return True
        return False

    def _are_contradictory(self, s1, s2):
        s1_norm = s1.lower().replace(' and ', ' ').replace(' or ', ' ').replace(' not ', ' ~')
        s2_norm = s2.lower().replace(' and ', ' ').replace(' or ', ' ').replace(' not ', ' ~')
        if s1_norm == '~' + s2_norm or s2_norm == '~' + s1_norm:
            return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    print(checker.check(['P', 'not P']))
    print(checker.check(['A and B', 'A or not B']))
    print(checker.check(['A and B', 'C or D']))