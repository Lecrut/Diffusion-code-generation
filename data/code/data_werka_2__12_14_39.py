class WeightConverter:
    KG_TO_POUNDS_CONSTANT = 2.2046226218487757

    @staticmethod
    def kg_to_pounds(kg):
        if not isinstance(kg, (int, float)):
            raise ValueError("Input must be a number")
        return kg * WeightConverter.KG_TO_POUNDS_CONSTANT

    @staticmethod
    def pounds_to_kg(pounds):
        if not isinstance(pounds, (int, float)):
            raise ValueError("Input must be a number")
        return pounds / WeightConverter.KG_TO_POUNDS_CONSTANT

if __name__ == '__main__':
    sample_kg = 70.5
    sample_pounds = 154.32
    converter = WeightConverter()
    
    try:
        converted_pounds = converter.kg_to_pounds(sample_kg)
        print(f"{sample_kg} kg is {converted_pounds:.2f} pounds")
    except ValueError as e:
        print(e)

    try:
        converted_kg = converter.pounds_to_kg(sample_pounds)
        print(f"{sample_pounds} pounds is {converted_kg:.2f} kg")
    except ValueError as e:
        print(e)