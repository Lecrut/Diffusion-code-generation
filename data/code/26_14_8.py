import sys

def is_above_threshold(value: float) -> bool:
    """Check if a value is strictly greater than 100."""
    return value > 100

class ThresholdGenerator:
    def __init__(self, threshold: float = 100):
        self.threshold = threshold

    def generate(self, sequence_iterable) -> bool:
        """Yield True only when the input value is strictly greater than the threshold."""
        for item in sequence_iterable:
            if isinstance(item, (int, float)):
                yield is_above_threshold(item)

if __name__ == '__main__':
    # Hard-coded sample values without user interaction or external dependencies
    samples = [50.0, 100.0, 99.9, 200.0]

    generator = ThresholdGenerator(threshold=100)

    print("Testing threshold generator:")
    for result in generator.generate(samples):
        if result:
            # Only process True results to demonstrate memory efficiency (no storage of all outputs)
            pass