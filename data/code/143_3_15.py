class ContradictionDetector:
    NEGATION_MAP = {'not': '', 'no': '', 'never': '', "don't": '', "can't": ''}

    @staticmethod
    def negate_keywords(text):
        for keyword, _ in ContradictionDetector.NEGATION_MAP.items():
            text = text.replace(keyword, '')
        return text.strip()

    @staticmethod
    def detect_conflicts(text1, text2):
        negated_text2 = ContradictionDetector.negate_keywords(text2)
        return text1 != negated_text2
if __name__ == '__main__':
    detector = ContradictionDetector()
    print(detector.detect_conflicts('I can do it', 'I cannot do it'))
    print(detector.detect_conflicts('It is sunny', 'It is not sunny'))