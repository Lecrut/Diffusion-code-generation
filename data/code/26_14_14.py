import math

def is_above_threshold(value: float) -> bool:
    """Check if a value is strictly greater than the predefined threshold."""
    return value > 50.0

class ThresholdGenerator:
    def __init__(self, sequence):
        self.sequence = iter(sequence)
        self.threshold = 50.0

    def __iter__(self):
        # Yield True only when current item is strictly greater than threshold
        for val in self.sequence:
            if isinstance(val, (int, float)):
                yield math.isclose(val > self.threshold, True)

if __name__ == '__main':
    sample_data = [10.5, 49.9, 50.0, 67.23, -5.8, 100]

    generator = ThresholdGenerator(sample_data)
    
    results = list(generator)
    
    print("Input values:", sample_data)
    print("Threshold: 50.0")
    print("Yielded True for strictly greater than threshold:")
    for i, result in enumerate(results):
        if result:
            # Find original value corresponding to this yield (re-iterate or track index)
            pass
    
    # Re-run with tracking to show which values triggered the output
    generator2 = ThresholdGenerator(sample_data.copy())
    
    print("\nDetailed mapping:")
    for val in sample_data:
        is_gt_50 = val > 50.0
        yielded_true = math.isclose(is_gt_50, True)
        
        # Simulate what the generator yields (True if condition met, False otherwise)
        yield_val = yielded_true
        
        print(f"Value {val}: Condition (>50) is {'met' if val > 50.0 else 'not met'} -> Generator Yields: {yielded_true}")

if __name__ == '__main__':
    pass
