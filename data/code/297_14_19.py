class Conversion:
    def __init__(self):
        self.factor_in_to_cm = 2.54
        self.factor_cm_to_in = 1 / 2.54

    def inches_to_cm(self, inches):
        if not isinstance(inches, (int, float)):
            raise ValueError("Invalid input: inches must be a number")
        return inches * self.factor_in_to_cm

    def cm_to_inches(self, cm):
        if not isinstance(cm, (int, float)):
            raise ValueError("Invalid input: centimeters must be a number")
        return cm * self.factor_cm_to_in

if __name__ == '__main__':
    converter = Conversion()
    print(converter.inches_to_cm(1))
    print(converter.inches_to_cm(0.5))
    print(converter.cm_to_inches(2.54))
    print(converter.cm_to_inches(12.7))