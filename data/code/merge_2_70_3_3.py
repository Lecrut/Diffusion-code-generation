import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def to_meters(self):
        return self.value * 1000 if isinstance(self, Kilometers) else self.value
class Meters(BaseMeasurement):
    pass
class Kilometers(BaseMeasurement):
    pass
class DistanceComparator:
    @staticmethod
    def compare_distance(obj_a, obj_b, metric='meters'):
        val_a = obj_a.to_meters() if metric == 'meters' else obj_a.value / 1000
        val_b = obj_b.to_meters() if metric == 'meters' else obj_b.value / 1000
        return {
            "distance_a": round(val_a, 4),
            "distance_b": round(val_b, 4),
            "difference": round(abs(val_a - val_b), 4),
            "is_equal_within_tolerance": abs(val_a - val_b) < 1e-6
        }
if __name__ == '__main__':
    d1 = Meters(50.234)
    d2 = Kilometers(0.051)
    result = DistanceComparator.compare_distance(d1, d2, metric='meters')
    print(result)