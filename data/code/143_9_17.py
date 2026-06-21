class LogicalOppositionChecker:
    NEGATION_MARKERS = {'not', 'no', 'never', 'none'}
    KEYWORDS = {'true', 'false'}

    @staticmethod
    def contains_negation(statement):
        return any(marker in statement.lower() for marker in LogicalOppositionChecker.NEGATION_MARKERS)

    @staticmethod
    def has_keyword(statement, keyword):
        return keyword.lower() in statement.lower()

    @classmethod
    def check_logical_opposition(cls, statement1, statement2):
        if cls.contains_negation(statement1) and cls.contains_negation(statement2):
            return False
        for keyword in cls.KEYWORDS:
            if (cls.has_keyword(statement1, keyword) and not cls.has_keyword(statement2, keyword)) or \
               (not cls.has_keyword(statement1, keyword) and cls.has_keyword(statement2, keyword)):
                return True
        return False

if __name__ == '__main__':
    checker = LogicalOppositionChecker()
    statement1 = "The sky is blue."
    statement2 = "The sky is not green."
    print(checker.check_logical_opposition(statement1, statement2))