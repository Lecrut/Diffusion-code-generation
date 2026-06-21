from typing import List, Optional

class Statistics:
    @staticmethod
    def compute_mean(data: List[float]) -> Optional[float]:
        if not data:
            return None
        return sum(data) / len(data)

if __name__ == '__main__':
    sample_data = [7.7, 8.8, 9.9]
    mean_value = Statistics.compute_mean(sample_data)
    print(mean_value)