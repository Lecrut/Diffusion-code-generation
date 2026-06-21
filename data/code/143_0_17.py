class ContradictionChecker:
    @staticmethod
    def check_contradiction(statement1, statement2):
        if statement1 == statement2:
            return False
        if 'not' in statement1 and statement1.replace('not ', '') in statement2:
            return True
        if 'not' in statement2 and statement2.replace('not ', '') in statement1:
            return True
        return False

if __name__ == '__main__':
    print(ContradictionChecker.check_contradiction('The sky is blue', 'The sky is not blue'))
    print(ContradictionChecker.check_contradiction('The sky is blue', 'The sky is green'))
    print(ContradictionChecker.check_contradiction('It will rain', 'It will not rain'))
    print(ContradictionChecker.check_contradiction('It will rain', 'It might rain'))