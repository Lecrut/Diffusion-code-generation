def _is_valid_positive_weight(raw_value):
    try:
        cleaned = str(raw_value).strip()
        if not cleaned:
            return False
        parsed = float(cleaned)
        if parsed <= 0:
            return False
        return True
    except ValueError:
        return False
    except TypeError:
        return False

def sanitize_weight_readings(readings):
    VALID_READINGS = []
    for reading in readings:
        if _is_valid_positive_weight(reading):
            VALID_READINGS.append(float(str(reading).strip()))
    return VALID_READINGS

class MeasurementValidator:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    
    def process(self):
        validated_list = []
        for item in self.raw_data:
            if _is_valid_positive_weight(item):
                validated_list.append(float(str(item).strip()))
        return validated_list

if __name__ == '__main__':
    test_data = ['42.5', '-10', '0', 'not_a_number', '  3.14  ', '', None, '7', '-0.5', '100']
    direct_result = sanitize_weight_readings(test_data)
    validator_instance = MeasurementValidator(test_data)
    class_result = validator_instance.process()
    print(direct_result)
    print(class_result)