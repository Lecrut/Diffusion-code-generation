import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = value
    def get_distance(self, other):
        return abs(self.value - other.value)
class DistanceObject(BaseMeasurement):
    pass
def compare_distances(obj1, obj2):
    distance = obj1.get_distance(obj2)
    comparison_result = {
        "distance": distance,
        "obj1_value": obj1.value,
        "obj2_value": obj2.value,
        "is_equal": math.isclose(obj1.value, obj2.value),
        "greater_than": obj1.value > obj2.value
    }
    return comparison_result
if __name__ == '__main__':
    d_obj_1 = DistanceObject(50.0)
    d_obj_2 = DistanceObject(48.7)
    result = compare_distances(d_obj_1, d_obj_2)
    print(result["distance"])