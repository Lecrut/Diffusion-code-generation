import math
class BaseMeasurement:
    def __init__(self, value):
        self.value = float(value)
    def get_distance(self, other):
        return abs(self.value - other.value)
class Distance(BaseMeasurement):
    pass
def compare_distances(obj1, obj2):
    dist_1_to_2 = obj1.get_distance(obj2)
    dist_2_to_1 = obj2.get_distance(obj1)
    result_dict = {
        "distance_obj1_to_obj2": round(dist_1_to_2, 4),
        "distance_obj2_to_obj1": round(dist_2_to_1, 4),
        "is_symmetric": dist_1_to_2 == dist_2_to_1,
    }
    return result_dict
if __name__ == '__main__':
    d_a = Distance(50)
    d_b = Distance(73.8)
    comparison_result = compare_distances(d_a, d_b)
    print(comparison_result)