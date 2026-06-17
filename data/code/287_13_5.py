from abc import ABC, abstractmethod
class WeightSystem(ABC):
    @abstractmethod
    def convert(self, weight):
        pass
class MetricSystem(WeightSystem):
    def convert(self, weight):
        return weight
class ImperialSystem(WeightSystem):
    def convert(self, weight):
        return weight
if __name__ == '__main__':
    metric = MetricSystem()
    imperial = ImperialSystem()
    sample_weight = 10
    metric_result = metric.convert(sample_weight)
    imperial_result = imperial.convert(sample_weight)
    print(f"Metric conversion of {sample_weight}: {metric_result}")
    print(f"Imperial conversion of {sample_weight}: {imperial_result}")