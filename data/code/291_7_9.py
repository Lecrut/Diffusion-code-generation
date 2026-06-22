class LengthComparator:
    MILE_TO_KILOMETER = 1.60934

    @staticmethod
    def miles_to_kilometers(miles):
        return miles * LengthComparator.MILE_TO_KILOMETER

    @staticmethod
    def kilometers_to_miles(kilometers):
        return kilometers / LengthComparator.MILE_TO_KILOMETER

if __name__ == '__main__':
    miles = 5
    kilometers = LengthComparator.miles_to_kilometers(miles)
    print(f"{miles} miles is {kilometers:.2f} kilometers")

    kilometers = 8
    miles = LengthComparator.kilometers_to_miles(kilometers)
    print(f"{kilometers} kilometers is {miles:.2f} miles")