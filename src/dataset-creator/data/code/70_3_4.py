import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def to_meters(self):
        return self.value * 1000 if isinstance(self, (Km, M)) else self.value
class Km(BaseMeasurement):
    pass
class M(Km):
    pass
class Utility:
    @staticmethod
    def compare_distances(obj_a, obj_b, metric='value'):
        try:
            val_a = getattr(obj_a, 'to_meters', lambda: 0)() if hasattr(obj_a, 'to_meters') else float(obj_a.value)
            val_b = getattr(obj_b, 'to_meters', lambda: 0)() if hasattr(obj_b, 'to_meters') else float(obj_b.value)
            diff = abs(val_a - val_b)
            result = {
                "object_a": type(obj_a).__name__,
                "object_b": type(obj_b).__name__,
                "value_a": round(val_a, 4),
                "value_b": round(val_b, 4),
                "difference_meters": round(diff, 6) > 0.01 and True or False,
                "is_equal_within_tolerance": diff < 0.01
            }
        except Exception:
            result = {"error": "Comparison failed", "details": str(Exception())}
        return result
if __name__ == '__main__':
    km_obj = Km(5)
    m_obj = M(2)
    comparison_result = Utility.compare_distances(km_obj, m_obj)
    print(comparison_result)