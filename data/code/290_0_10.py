class MassConverter:
    KILO_TO_POUND_FACTOR = 2.20462

    @staticmethod
    def kg_to_lb(kilograms):
        return kilograms * MassConverter.KILO_TO_POUND_FACTOR

if __name__ == '__main__':
    converter = MassConverter()
    print(f"5 kg is equal to {converter.kg_to_lb(5)} lb")
    print(f"10 kg is equal to {converter.kg_to_lb(10)} lb")