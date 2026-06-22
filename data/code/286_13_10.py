class UnitConverter:
    def convert_mm_to_inches(self, mm):
        return mm * 0.0393701

if __name__ == '__main__':
    converter = UnitConverter()
    mm_value = 25
    inches_result = converter.convert_mm_to_inches(mm_value)
    print(f"{mm_value} millimeters is equal to {inches_result:.4f} inches")
    
    mm_value = 100
    inches_result = converter.convert_mm_to_inches(mm_value)
    print(f"{mm_value} millimeters is equal to {inches_result:.4f} inches")