def _parse_positive_weight(raw_value):
    cleaned = str(raw_value).strip()
    if not cleaned:
        raise ValueError("Empty input")
    parsed = float(cleaned)
    if parsed <= 0:
        raise ValueError("Non-positive value")
    return parsed

class WeightProcessor:
    def __init__(self, measurements):
        self.measurements = measurements
    def get_valid_weights(self):
        results = []
        for item in self.measurements:
            try:
                results.append(_parse_positive_weight(item))
            except (ValueError, TypeError):
                continue
        return results

if __name__ == '__main__':
    sample_inputs = ['10.5', '-3.2', '0', 'abc', '25', '', '7.89', '  4.5  ', 'null']
    processor = WeightProcessor(sample_inputs)
    print(processor.get_valid_weights())