class MilesToFeetConverter:
    def convert(self, miles):
        feet_per_mile = 5280
        return miles * feet_per_mile

if __name__ == '__main__':
    converter = MilesToFeetConverter()
    sample_miles = 3.5
    result = converter.convert(sample_miles)
    print(result)