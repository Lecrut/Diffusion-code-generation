class NumberRanker:
    DEFAULT_SAMPLE_VALUES = [34, 56, 23, 89, 12, 45]

    @staticmethod
    def determine_the_largest_number_present_rank_samples():
        sample_values = NumberRanker.DEFAULT_SAMPLE_VALUES
        sorted_values = sorted(sample_values, reverse=True)
        return sorted_values

if __name__ == '__main__':
    result = NumberRanker.determine_the_largest_number_present_rank_samples()
    print(result)