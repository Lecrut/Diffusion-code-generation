class MilesToFeetConverter:
    def __init__(self):
        self.conversion_factor = 5280

    def convert(self, miles):
        return miles * self.conversion_factor

if __name__ == '__main__':
    converter = MilesToFeetConverter()
    miles = 1.0
    feet = converter.convert(miles)
    print(feet)