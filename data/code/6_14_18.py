class WeightMetric:
    def __init__(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Weight must be a numeric type")
        if value < 0:
            raise ValueError("Weight cannot be negative")
        self.value = value

    def get_value(self):
        return self.value

def compute_weight_difference(w1, w2):
    metric1 = WeightMetric(w1)
    metric2 = WeightMetric(w2)
    val1 = metric1.get_value()
    val2 = metric2.get_value()
    diff = val1 - val2
    return abs(diff)

if __name__ == '__main__':
    initial = 200.0
    final = 175.5
    result = compute_weight_difference(initial, final)
    print(result)