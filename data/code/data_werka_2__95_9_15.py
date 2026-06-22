class CheckSummarizer:
    POSITIVE_LABEL = "positive"
    EVEN_LABEL = "even"
    LESS_THAN_100_LABEL = "less than 100"
    EMPTY_RESULT = "none met"
    SEPARATOR = ", "

    @staticmethod
    def _get_label(is_condition, label):
        if is_condition:
            return label
        return None

    @staticmethod
    def _format_results(items):
        valid_items = [item for item in items if item is not None]
        if not valid_items:
            return CheckSummarizer.EMPTY_RESULT
        return CheckSummarizer.SEPARATOR.join(valid_items)

    def combine_checks(self, is_positive, is_even, is_less_than_100):
        labels = [
            self._get_label(is_positive, self.POSITIVE_LABEL),
            self._get_label(is_even, self.EVEN_LABEL),
            self._get_label(is_less_than_100, self.LESS_THAN_100_LABEL)
        ]
        return self._format_results(labels)

if __name__ == '__main__':
    summarizer = CheckSummarizer()
    result1 = summarizer.combine_checks(True, True, True)
    print(result1)
    result2 = summarizer.combine_checks(False, False, False)
    print(result2)
    result3 = summarizer.combine_checks(True, False, False)
    print(result3)