class WeightConverter:
    GRAMS_TO_OUNCES = 0.035274

    @staticmethod
    def grams_to_ounces(grams: float) -> float:
        return round(grams * WeightConverter.GRAMS_TO_OUNCES, 2)

if __name__ == '__main__':
    weights_in_grams = [100, 200, 300]
    weights_in_ounces = [WeightConverter.grams_to_ounces(weight) for weight in weights_in_grams]
    print(weights_in_ounces)