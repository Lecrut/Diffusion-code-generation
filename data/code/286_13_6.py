class MillimeterConverter:
    def __init__(self):
        self.factor = 0.0393701

    def convert_mm_to_inches(self, mm):
        return mm * self.factor

if __name__ == '__main__':
    converter = MillimeterConverter()
    sample_values = [25, 100]
    for value in sample_values:
        inches = converter.convert_mm_to_inches(value)
        print(f"{value} millimeters is equal to {inches:.4f} inches")