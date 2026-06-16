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
            raise ValueError("Unsupported conversion: " + from_system + " to " + to_system)
class ImperialSystem(WeightSystem):
    def convert(self, weight: float, from_system: str, to_system: str) -> float:
        if from_system == "Imperial" and to_system == "Metric":
            return weight * 0.453592
        elif from_system == "Metric" and to_system == "Imperial":
            return weight / 0.453592
        elif from_system == to_system:
            return weight
        else:
            raise ValueError("Unsupported conversion: " + from_system + " to " + to_system)
if __name__ == '__main__':
    metric = MetricSystem()
    imperial = ImperialSystem()
    sample_weight = 10.0
    print(f"--- Testing Metric System ---")
    metric_result = metric.convert(sample_weight, "Metric", "Metric")
    print(f"{sample_weight} Metric to Metric: {metric_result}")
    metric_to_imperial = metric.convert(sample_weight, "Metric", "Imperial")
    print(f"{sample_weight} Metric to Imperial: {metric_to_imperial:.2f}")
    print(f"\n--- Testing Imperial System ---")
    imperial_result = imperial.convert(sample_weight, "Imperial", "Imperial")
    print(f"{sample_weight} Imperial to Imperial: {imperial_result}")
    imperial_to_metric = imperial.convert(sample_weight, "Imperial", "Metric")
    print(f"{sample_weight} Imperial to Metric: {imperial_to_metric:.2f}")