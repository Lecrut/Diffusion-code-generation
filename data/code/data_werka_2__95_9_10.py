class CheckSummarizer:
    LABELS = ("positive", "even", "less than 100")
    SEPARATOR = " and "
    EMPTY_RESULT = "no conditions met"

    @staticmethod
    def _get_label(index):
        return CheckSummarizer.LABELS[index]

    @staticmethod
    def combine_checks(is_positive, is_even, is_less_than_100):
        flags = (is_positive, is_even, is_less_than_100)
        matched_labels = []
        for i, flag in enumerate(flags):
            if flag:
                matched_labels.append(CheckSummarizer._get_label(i))
        if not matched_labels:
            return CheckSummarizer.EMPTY_RESULT
        return CheckSummarizer.SEPARATOR.join(matched_labels)

if __name__ == '__main__':
    print(CheckSummarizer.combine_checks(True, True, True))
    print(CheckSummarizer.combine_checks(False, False, False))
    print(CheckSummarizer.combine_checks(True, False, True))