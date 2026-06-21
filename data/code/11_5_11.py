class LastItemFinder:
    EMPTY_RESULT = None

    @staticmethod
    def find_last(item_sequence):
        result = LastItemFinder.EMPTY_RESULT
        for element in item_sequence:
            result = element
        return result

if __name__ == '__main__':
    sample_values = [100, 200, 300]
    outcome = LastItemFinder.find_last(sample_values)
    print(outcome)