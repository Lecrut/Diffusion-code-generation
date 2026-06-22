class MilesToFeetConverter:
    def __init__(self):
        self.feet_per_mile = 5280

    def convert(self, miles):
        return miles * self.feet_per_mile

if __name__ == '__main__':
    converter = MilesToFeetConverter()
    result = converter.convert(2)
    print(result)