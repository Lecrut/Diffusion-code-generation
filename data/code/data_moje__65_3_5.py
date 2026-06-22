class FootConverter:
    INCHES_PER_FOOT = 12

    def __init__(self, feet_value):
        self.feet = feet_value

    def to_inches(self):
        return self.feet * self.INCHES_PER_FOOT

    def to_yards(self):
        return self.feet / 3.0

    def to_centimeters(self):
        return self.feet * 30.48

if __name__ == '__main__':
    converter = FootConverter(10)
    inches = converter.to_inches()
    yards = converter.to_yards()
    cm = converter.to_centimeters()
    print(inches)
    print(yards)
    print(cm)