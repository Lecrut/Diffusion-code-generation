class ContradictionChecker:
    NOT = 'not'

    @staticmethod
    def is_contradictory(s1, s2):
        s1_lower = s1.lower()
        s2_lower = s2.lower()
        if ContradictionChecker.NOT in s1_lower and s2_lower.replace(ContradictionChecker.NOT, '').strip() == s1_lower[3:].strip():
            return True
        if ContradictionChecker.NOT in s2_lower and s1_lower.replace(ContradictionChecker.NOT, '').strip() == s2_lower[3:].strip():
            return True
        return False

    def check(self, statements):
        n = len(statements)
        for i in range(n):
            for j in range(i + 1, n):
                if self.is_contradictory(statements[i], statements[j]):
                    return True
        return False
if __name__ == '__main__':
    checker = ContradictionChecker()
    print(checker.check(['P', 'not P']))
    print(checker.check(['A', 'B']))