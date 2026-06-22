def parse_weight_measurement(raw_input):
    cleaned = str(raw_input).strip()
    if not cleaned:
        raise ValueError("Empty string provided")
    value = float(cleaned)
    if value <= 0:
        raise ValueError("Weight must be positive")
    return value

def sanitize_weight_list(measurements):
    valid_weights = []
    for entry in measurements:
        try:
            valid_weights.append(parse_weight_measurement(entry))
        except (ValueError, TypeError, AttributeError):
            continue
    return valid_weights

class WeightValidator:
    def __init__(self, raw_data):
        self.raw_data = raw_data
    
    def get_positive_weights(self):
        cleaned_list = []
        for item in self.raw_data:
            try:
                cleaned_list.append(parse_weight_measurement(item))
            except (ValueError, TypeError, AttributeError):
                continue
        return cleaned_list

if __name__ == '__main__':
    test_cases = ["12.5", "0", "-4.2", "abc", "  3.14  ", None, "", "100", "inf", "-0.0"]
    validator = WeightValidator(test_cases)
    print(validator.get_positive_weights())
    
    raw_list = ["5", "invalid", "0.0", "7.5", "-10", ""]
    print(sanitize_weight_list(raw_list))