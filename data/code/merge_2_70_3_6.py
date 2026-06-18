import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def to_meters(self):
        return self.value * 100 if isinstance(self, Kilometers) else self.value
class Meters(BaseMeasurement):
    pass
class Kilometers(BaseMeasurement):
    pass
class DistanceComparator:
    @staticmethod
    def compare_distances(obj_a, obj_b):
        meters_a = obj_a.to_meters()
        meters_b = obj_b.to_meters()
        if abs(meters_a - meters_b) < 0.01:
            return "Equal"
        elif meters_a > meters_b:
            return f"{obj_a.__class__.__name__} is larger by {meters_a - meters_b:.2f} m"
        else:
            return f"{obj_b.__class__.__name__} is larger by {meters_b - meters_a:.2f} m"
if __name__ == '__main__':
    d1 = Meters(50)
    d2 = Kilometers(0.5001)
    result = DistanceComparator.compare_distances(d1, d2)
    print(result)