from abc import ABC, abstractmethod
class WeightSystem(ABC):
    @abstractmethod
    def convert(self, weight: float, from_system: str, to_system: str) -> float:
        pass
class MetricSystem(WeightSystem):
    def convert(self, weight: float, from_system: str, to_system: str) -> float:
        if from_system == "Metric" and to_system == "Imperial":
            return weight * 1.48815
        elif from_system == "Imperial" and to_system == "Metric":
            return weight / 1.48815
        elif from_system == to_system:
            return weight
        else:
            raise ValueError("Unsupported conversion between specified systems")
class ImperialSystem(WeightSystem):
    def convert(self, weight: float, from_system: str, to_system: str) -> float:
        if from_system == "Imperial" and to_system == "Metric":
            return weight * 0.453592
        elif from_system == "Metric" and to_system == "Imperial":
            return weight / 0.453592
        elif from_system == to_system:
            return weight
        else:
            raise ValueError("Unsupported conversion between specified systems")
if __name__ == '__main__':
    metric = MetricSystem()
    imperial = ImperialSystem()
    sample_weight = 10.0
    print(f"Original Weight: {sample_weight}")
    try:
        result_m_to_i = metric.convert(sample_weight, "Metric", "Imperial")
        print(f"Conversion from Metric to Imperial: {result_m_to_i:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_i_to_m = imperial.convert(sample_weight, "Imperial", "Metric")
        print(f"Conversion from Imperial to Metric: {result_i_to_m:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result_same = metric.convert(sample_weight, "Metric", "Metric")
        print(f"Conversion from Metric to Metric: {result_same:.2f}")
    except ValueError as e:
        print(f"Error: {e}")