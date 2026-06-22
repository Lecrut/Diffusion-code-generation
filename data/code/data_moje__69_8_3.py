class MileToFeetConverter:
    def __init__(self):
        self.feet_per_mile = 5280

    def convert(self, miles):
        return miles * self.feet_per_mile

if __name__ == '__main__':
    converter = MileToFeetConverter()
    sample_miles = 10.0
    result = converter.convert(sample_miles)
    print(result)