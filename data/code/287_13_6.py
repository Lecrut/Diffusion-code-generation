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
            raise ValueError("Unsupported conversion from Metric system.")
class ImperialSystem(WeightSystem):
    def convert(self, weight: float, from_system: str, to_system: str) -> float:
        if from_system == "Imperial" and to_system == "Metric":
            return weight * 0.453592
        elif from_system == "Metric" and to_system == "Imperial":
            return weight / 0.453592
        elif from_system == to_system:
            return weight
        else:
            raise ValueError("Unsupported conversion from Imperial system.")
if __name__ == '__main__':
    metric = MetricSystem()
    imperial = ImperialSystem()
    sample_weight = 10.0
    print(f"--- Testing Metric System ---")
    metric_result_to_imperial = metric.convert(sample_weight, "Metric", "Imperial")
    print(f"{sample_weight} Metric units is approximately {metric_result_to_imperial:.2f} Imperial units.")
    metric_result_to_metric = metric.convert(sample_weight, "Metric", "Metric")
    print(f"{sample_weight} Metric units converted to Metric: {metric_result_to_metric}")
    print(f"\n--- Testing Imperial System ---")
    imperial_result_to_metric = imperial.convert(sample_weight, "Imperial", "Metric")
    print(f"{sample_weight} Imperial units is approximately {imperial_result_to_metric:.2f} Metric units.")
    imperial_result_to_imperial = imperial.convert(sample_weight, "Imperial", "Imperial")
    print(f"{sample_weight} Imperial units converted to Imperial: {imperial_result_to_imperial}")