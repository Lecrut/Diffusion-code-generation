from abc import ABC, abstractmethod
class WeightSystem(ABC):
    @abstractmethod
    def convert_to_kg(self, weight):
        pass
class MetricSystem(WeightSystem):
    def convert_to_kg(self, weight):
        return weight
class ImperialSystem(WeightSystem):
    def convert_to_kg(self, weight):
        return weight * 0.453592
if __name__ == '__main__':
    metric = MetricSystem()
    imperial = ImperialSystem()
    sample_weight_metric = 10
    sample_weight_imperial = 10
    kg_from_metric = metric.convert_to_kg(sample_weight_metric)
    kg_from_imperial = imperial.convert_to_kg(sample_weight_imperial)
    print(f"Metric System conversion: {kg_from_metric} kg")
    print(f"Imperial System conversion: {kg_from_imperial} kg")