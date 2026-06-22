class LengthConverter:
    INCHES_PER_FOOT = 12
    def __init__(self, feet):
        self.feet = feet
    def to_inches(self):
        return self.feet * self.INCHES_PER_FOOT
    def get_feet(self):
        return self.feet

if __name__ == '__main__':
    converter = LengthConverter(5)
    print(converter.to_inches())