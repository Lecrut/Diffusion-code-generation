class WeightConverter:
    OUNCES_PER_POUND = 16.0

    def convert_pounds_to_ounces(self, pounds):
        return pounds * self.OUNCES_PER_POUND

    def convert_kilograms_to_ounces(self, kilograms):
        return kilograms * (self.OUNCES_PER_POUND / 0.453592)

def combine_weights(pounds_list, kilograms_list):
    converter = WeightConverter()
    ounces_list = [converter.convert_pounds_to_ounces(p) for p in pounds_list]
    ounces_list.extend([converter.convert_kilograms_to_ounces(k) for k in kilograms_list])
    return ounces_list

if __name__ == '__main__':
    pounds = [10, 20, 30]
    kilograms = [5, 7.5]
    result = combine_weights(pounds, kilograms)
    print(result)