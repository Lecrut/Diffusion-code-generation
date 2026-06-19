class WeightConverter:
    def __init__(self, weight, unit):
        self.weight = weight
        self.unit = unit

    @classmethod
    def convert_unit(cls, instance, new_unit):
        if instance.unit == 'pounds' and new_unit == 'kilograms':
            instance.weight *= 0.453592
            instance.unit = new_unit
        elif instance.unit == 'kilograms' and new_unit == 'pounds':
            instance.weight /= 0.453592
            instance.unit = new_unit

    def __str__(self):
        return f"{self.weight} {self.unit}"

if __name__ == '__main__':
    weight_in_pounds = WeightConverter(180, 'pounds')
    print(weight_in_pounds)
    
    WeightConverter.convert_unit(weight_in_pounds, 'kilograms')
    print(weight_in_pounds)

    weight_in_kilograms = WeightConverter(81.647, 'kilograms')
    print(weight_in_kilograms)
    
    WeightConverter.convert_unit(weight_in_kilograms, 'pounds')
    print(weight_in_kilograms)