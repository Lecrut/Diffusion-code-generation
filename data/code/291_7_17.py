class LengthComparator:
    def __init__(self):
        self.conversion_factor = 1.60934

    def miles_to_kilometers(self, miles):
        return miles * self.conversion_factor

    def kilometers_to_miles(self, kilometers):
        return kilometers / self.conversion_factor

if __name__ == '__main__':
    comparator = LengthComparator()
    sample_miles = 5
    sample_kilometers = 8.04672
    
    print(f"{sample_miles} miles is equal to {comparator.miles_to_kilometers(sample_miles):.2f} kilometers")
    print(f"{sample_kilometers} kilometers is equal to {comparator.kilometers_to_miles(sample_kilometers):.2f} miles")