class SemanticAnalyzer:

    def __init__(self):
        self.statements = []

    def add_statement(self, statement):
        self.statements.append(statement)

    def are_mutually_exclusive(self):
        for i in range(len(self.statements)):
            for j in range(i + 1, len(self.statements)):
                if self._is_contradiction(self.statements[i], self.statements[j]):
                    return True
        return False

    def _is_contradiction(self, statement1, statement2):
        return 'not' in statement1.lower() and statement1.replace(' not', '') == statement2
if __name__ == '__main__':
    analyzer = SemanticAnalyzer()
    analyzer.add_statement('The sky is blue.')
    analyzer.add_statement('The sky is not green.')
    print(analyzer.are_mutually_exclusive())