import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def to_meters(self):
        return self.value * 1000
    def __eq__(self, other):
        if not isinstance(other, BaseMeasurement):
            return False
        return abs(self.to_meters() - other.to_meters()) < 1e-6
class Distance(BaseMeasurement):
    pass
def compare_distances(d1: BaseMeasurement, d2: BaseMeasurement) -> dict:
    result = {
        "d1_value": round(d1.to_meters(), 4),
        "d2_value": round(d2.to_meters(), 4),
        "difference": abs(round((d1 - d2).to_meters()), 4) if hasattr(type(d1).__subclasses__, '__mro__') else None,                                                       
    }
    try:
        diff = (d1.to_meters() - d2.to_meters())
        result["difference"] = round(diff, 4)
        if abs(diff) < 0.01:
            result["equal"] = True
        else:
            result["equal"] = False
        m1 = d1.to_meters()
        m2 = d2.to_meters()
        if m1 > m2:
            result["winner"] = "d1"
        elif m2 > m1:
            result["winner"] = "d2"
        else:
            result["winner"] = None
    except AttributeError:
        pass
    return result
if __name__ == '__main__':
    d1 = Distance(0.5)              
    d2 = Distance(499)               
    comparison_result = compare_distances(d1, d2)
    print(comparison_result)