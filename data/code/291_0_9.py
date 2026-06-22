class MeterComparator:
    METERS_TO_INCHES = 39.3701

    @staticmethod
    def convert_to_inches(meters):
        return meters * MeterComparator.METERS_TO_INCHES

    @staticmethod
    def compare_lengths(length1, length2):
        length1_in_inches = MeterComparator.convert_to_inches(length1)
        length2_in_inches = MeterComparator.convert_to_inches(length2)

        if length1 > length2:
            return f"{length1} meters is longer than {length2} meters."
        elif length2 > length1:
            return f"{length2} meters is longer than {length1} meters."
        else:
            return f"Both lengths are equal: {length1} meters."

if __name__ == '__main__':
    sample_length1 = 5
    sample_length2 = 3.5
    result = MeterComparator.compare_lengths(sample_length1, sample_length2)
    print(result)

    another_sample_length1 = 4
    another_sample_length2 = 4
    result2 = MeterComparator.compare_lengths(another_sample_length1, another_sample_length2)
    print(result2)