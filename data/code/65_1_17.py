INCHES_PER_FOOT = 12

class LengthConverter:
    def __init__(self, feet):
        self.feet = feet

    def to_inches(self):
        return self.feet * INCHES_PER_FOOT

    def description(self):
        return f"{self.feet} feet is {self.to_inches()} inches"

if __name__ == '__main__':
    sample_feet = 10
    converter = LengthConverter(sample_feet)
    inches_result = converter.to_inches()
    desc_result = converter.description()
    print(inches_result)
    print(desc_result)