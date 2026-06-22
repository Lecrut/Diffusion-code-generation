class LengthComparator:
    MILE_TO_KILOMETER = 1.60934

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * LengthComparator.MILE_TO_KILOMETER

    @staticmethod
    def compare_lengths(length1, unit1, length2, unit2):
        if unit1 == "miles" and unit2 == "kilometers":
            return length1 < length2
        elif unit1 == "kilometers" and unit2 == "miles":
            return length1 * LengthComparator.MILE_TO_KILOMETER < length2
        else:
            raise ValueError("Unsupported units")

if __name__ == '__main__':
    result = LengthComparator.compare_lengths(5, "miles", 8, "kilometers")
    print(result)