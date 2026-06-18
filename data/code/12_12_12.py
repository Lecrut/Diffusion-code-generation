import statistics

class WeightRatioConverter:
    """A class to convert a list of weight ratios into a normalized weight distribution."""

    def __init__(self, weights):
        if not isinstance(weights, (list, tuple)) or len(weights) == 0:
            raise ValueError("Input must be a non-empty list or tuple of numbers.")
        
        self.raw_ratios = [float(w) for w in weights]
    
    def convert(self):
        """Converts the weight ratios into normalized values where sum equals 1.0."""
        total_weight = sum(self.raw_ratios)
        if total_weight == 0:
            raise ValueError("Total weight is zero; normalization impossible.")

        return [ratio / total_weight for ratio in self.raw_ratios]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [[10, 20], [30, 40, 50], ['a', 'b']]

    try:
        converter = WeightRatioConverter(samples)
        
        print("=== Processing Sample Sets ===")
        
        # Process first sample (integers representing weight parts)
        result1 = converter.convert()
        print(f"Input Set [10, 20]: Normalized Distribution -> {result1}")

        # Process second sample (larger integers)
        raw_ratios_2 = [30.5, 40.75, 50]
        
        converter_two = WeightRatioConverter(raw_ratios_2)
        result2 = converter_two.convert()
        print(f"Input Set {raw_ratios_2}: Normalized Distribution -> {result2}")

    except Exception as e:
        print(f"Error during conversion process: {e}")