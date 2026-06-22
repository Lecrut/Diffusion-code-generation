class ScoreStatistics:
    EMPTY_LIST_VALUE = 0.0

    @staticmethod
    def validate_input(scores):
        if not scores or len(scores) == 0:
            return False
        for val in scores:
            if not isinstance(val, (int, float)):
                return False
        return True

    @staticmethod
    def calculate_mean(scores):
        if not ScoreStatistics.validate_input(scores):
            return ScoreStatistics.EMPTY_LIST_VALUE
        running_sum = 0.0
        number_of_elements = 0
        for s in scores:
            running_sum += float(s)
            number_of_elements += 1
        return running_sum / number_of_elements

if __name__ == '__main__':
    exam_results = [95, 87, 92, 88, 76, 94]
    average = ScoreStatistics.calculate_mean(exam_results)
    print(average)