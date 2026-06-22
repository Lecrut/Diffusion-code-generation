class MilesToFeetConverter:
    def __init__(self, miles):
        self.miles = miles

    def convert(self):
        return self.miles * 5280

if __name__ == '__main__':
    converter = MilesToFeetConverter(1)
    print(converter.convert())
    converter2 = MilesToFeetConverter(2.5)
    print(converter2.convert())