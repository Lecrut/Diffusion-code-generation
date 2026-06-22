class MileToFeetConverter:
    FEET_PER_MILE = 5280

    def convert(self, miles):
        if miles < 0:
            raise ValueError("Miles cannot be negative")
        return miles * self.FEET_PER_MILE

if __name__ == '__main__':
    converter = MileToFeetConverter()
    sample_miles = 3
    result = converter.convert(sample_miles)
    print(result)