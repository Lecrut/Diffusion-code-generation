class MillimeterToInchConverter:
    conversion_factor = 0.0393701

    def convert_mm_to_inches(self, mm):
        return mm * self.conversion_factor

if __name__ == '__main__':
    converter = MillimeterToInchConverter()
    sample_values = [25, 100]
    for value in sample_values:
        inches_result = converter.convert_mm_to_inches(value)
        print(f"{value} mm is equal to {inches_result:.4f} inches")