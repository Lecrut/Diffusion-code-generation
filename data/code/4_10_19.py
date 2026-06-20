class DistanceConverter:
    MILES_TO_KILOMETERS = 1.60934
    KILOMETERS_TO_MILES = 1 / 1.60934

    def convert(self, value, from_unit, to_unit):
        if not isinstance(value, (int, float)):
            raise ValueError("Input value must be a number")
        if value < 0:
            raise ValueError("Distance cannot be negative")
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()
        
        if from_unit_lower == to_unit_lower:
            return value
            
        if from_unit_lower == 'mile' or from_unit_lower == 'miles':
            if to_unit_lower == 'kilometer' or to_unit_lower == 'kilometers':
                return value * self.MILES_TO_KILOMETERS
            else:
                raise ValueError("Invalid target unit")
        elif from_unit_lower == 'kilometer' or from_unit_lower == 'kilometers':
            if to_unit_lower == 'mile' or to_unit_lower == 'miles':
                return value * self.KILOMETERS_TO_MILES
            else:
                raise ValueError("Invalid target unit")
        else:
            raise ValueError("Invalid source unit")

if __name__ == '__main__':
    converter = DistanceConverter()
    miles_value = 10.0
    km_value = 50.0
    
    result_m_to_k = converter.convert(miles_value, 'miles', 'kilometers')
    result_k_to_m = converter.convert(km_value, 'kilometers', 'miles')
    
    print(result_m_to_k)
    print(result_k_to_m)