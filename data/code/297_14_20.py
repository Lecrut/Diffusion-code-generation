class Conversion:
    INCHES_TO_CM = 2.54
    CM_TO_INCHES = 1 / 2.54

    def inches_to_cm(self, inches):
        return inches * self.INCHES_TO_CM

    def cm_to_inches(self, cm):
        return cm * self.CM_TO_INCHES

if __name__ == '__main__':
    converter = Conversion()
    print(converter.inches_to_cm(1))
    print(converter.inches_to_cm(0.5))
    print(converter.cm_to_inches(2.54))
    print(converter.cm_to_inches(12.7))