import threading
FACTORS = {
    "km": 0.001,
    "cm": 100.0,
    "mm": 1000.0,
    "inch": 39.3701,
}
class MetricConverter:
    def __init__(self):
        self._lock = threading.Lock()
    def convert(self, meters: float) -> dict:
        with self._lock:
            return {unit: meters * factor for unit, factor in FACTORS.items()}
if __name__ == '__main__':
    converter = MetricConverter()
    sample_values = [1.5, 200]
    results = {}
    for val in sample_values:
        key = f"Input: {val} m"
        results[key] = converter.convert(val)
    print(results)