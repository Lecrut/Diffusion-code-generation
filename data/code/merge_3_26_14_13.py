import math

def greater_than_threshold(value: float) -> bool:
    """Check if a value is strictly greater than a predefined threshold."""
    return value > 100.5

class ThresholdGenerator:
    def __init__(self, sequence):
        self.sequence = iter(sequence)
        self.threshold = 100.5

    def __iter__(self):
        for item in self.sequence:
            if greater_than_threshold(item):
                yield True
            # If the condition is not met, we do nothing (yield False implicitly by skipping),
            # but based on "yields True only when...", yielding None or doing nothing 
            # effectively filters. However, to strictly follow "generates a stream of booleans",
            # let's yield False otherwise if the expectation implies a boolean stream per input item.
            # Re-reading: "yields True only when...". This usually implies filtering (yielding None or just True).
            # But often in such tasks, it means yielding a sequence where each element corresponds to an input check result.
            # Let's assume the latter for completeness of data flow unless specified as a filter-only generator.
            if item > self.threshold:
                yield True
            else:
                yield False

if __name__ == '__main__':
    sample_data = [50, 120, -10, 99.6, 200, 100.4]

    gen = ThresholdGenerator(sample_data)
    
    print("Input -> Output:")
    for item in sample_data:
        result = next(gen) if hasattr(next, '__iter__') else False # Fallback logic not needed here as we iterate manually below
        
    # Re-iterate cleanly to show results
    gen2 = ThresholdGenerator(sample_data)
    print("\nResults (True/False):")
    for item in sample_data:
        result = next(gen2) if True else None