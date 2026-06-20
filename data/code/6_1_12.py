class WeightCalculator:
    BASE_UNITS = 1000
    MIN_WEIGHT = 0.0

    def __init__(self):
        self._history = list()

    def _normalize(self, weight_value):
        converted = float(weight_value)
        if converted < self.MIN_WEIGHT:
            converted = self.MIN_WEIGHT
        return converted

    def compute_weight_gap(self, source_mass, target_mass):
        norm_source = self._normalize(source_mass)
        norm_target = self._normalize(target_mass)
        difference = norm_target - norm_source
        self._history.append((source_mass, target_mass, difference))
        return difference

if __name__ == '__main__':
    machine = WeightCalculator()
    start = 45.5
    end = 70.2
    calculated_gap = machine.compute_weight_gap(start, end)
    print(calculated_gap)