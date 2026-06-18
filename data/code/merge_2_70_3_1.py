import math
from abc import ABC, abstractmethod
class BaseMeasurement(ABC):
    def __init__(self, value: float):
        self.value = value
    @abstractmethod
    def get_distance(self) -> float:
        pass
class DistanceObject(BaseMeasurement):
    def __init__(self, x1: float, y1: float, x2: float, y2: float):
        super().__init__(0.0)
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
    def get_distance(self) -> float:
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
class MeasurementComparator:
    @staticmethod
    def compare_distances(objs: list[BaseMeasurement]) -> dict[str, list[float]]:
        results = {
            "objects": [obj.get_distance() for obj in objs],
            "min_value": min([obj.get_distance() for obj in objs]),
            "max_value": max([obj.get_distance() for obj in objs]),
            "avg_value": sum([obj.get_distance() for obj in objs]) / len(objs) if objs else 0.0,
        }
        return results
if __name__ == '__main__':
    d1 = DistanceObject(0, 0, 3, 4)
    d2 = DistanceObject(0, 0, 5, 12)
    d3 = DistanceObject(-1, -1, 1, 1)
    comparator = MeasurementComparator()
    comparison_data = comparator.compare_distances([d1, d2, d3])