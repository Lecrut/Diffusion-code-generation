import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def get_value(self):
        return self.value
class Distance(BaseMeasurement):
    pass
def compare_distances(d1, d2):
    v1 = d1.get_value()
    v2 = d2.get_value()
    result = {
        "distance_1": v1,
        "distance_2": v2,
        "difference": abs(v1 - v2),
        "is_equal_within_tolerance": math.isclose(v1, v2, rel_tol=1e-9)
    }
    if result["difference"] > 0:
        result["winner"] = d1.get_value() if d1.get_value() < d2.get_value() else d2.get_value()
        result["comparison_type"] = "less_than" if v1 < v2 else "greater_than"
    else:
        result["winner"] = None
        result["comparison_type"] = "equal"
    return result
if __name__ == '__main__':
    d_obj_1 = Distance(5.0)
    d_obj_2 = Distance(3.7)
    comparison_result = compare_distances(d_obj_1, d_obj_2)
    print(comparison_result)