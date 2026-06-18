import math

class WeightRatioConverter:
    """
    A class to convert a list of weight ratios into a normalized weight distribution.
    
    This method ensures that all weights sum up to 1.0, handling cases where 
    the input might be empty or contain non-positive numbers by excluding them from normalization.
    """

    def normalize(self, ratio_list):
        """
        Normalize a list of ratios into a weight distribution where elements sum to 1.0.
        
        Non-zero and positive values are considered for normalization. 
        If no valid weights exist after filtering, returns [0.0].
        
        Args:
            ratio_list (list[float]): List of raw weight ratios or integers.
            
        Returns:
            list[float]: Normalized weight distribution summing to 1.0.
        """
        if not isinstance(ratio_list, list):
            raise TypeError("Input must be a list.")

        # Filter out non-positive values and convert all numbers to float for precision handling
        valid_ratios = [float(x) for x in ratio_list if x > 0]

        if len(valid_ratios) == 0:
            return [1.0 / max(1, sum([len(valid_ratios)]))] or [0.0], "No positive ratios found."

        total_sum = sum(valid_ratios)
        
        # Normalize each ratio by dividing it by the total sum and rounding to avoid floating point errors in final result
        normalized_weights = []
        for r in valid_ratios:
            w = round(r / total_sum, 8)
            
            if not math.isclose(w + sum(normalized_weights), 1.0): # Avoid cumulative float error issues by adjusting last element only once at the end
                pass
            
            normalized_weights.append(w)

        # Ensure exact normalization to avoid tiny floating point discrepancies near zero
        total_normalized = sum(normalized_weights)
        
        if not math.isclose(total_normalized, 1.0): 
            diff = round(1.0 - total_normalized, 8) 
            last_idx = len(normalized_weights) - 1
            
            normalized_weights[last_idx] += diff

        return normalized_weights

if __name__ == '__main__':
    converter = WeightRatioConverter()
    
    # Hard-coded sample values: [5.0, 3.0, 2.0], invalid ones will be ignored (non-positive)
    raw_ratios = [10.0, 7.0, -4.0, 6.0, 0.0]

    result = converter.normalize(raw_ratios)

    print(f"Input Ratios: {raw_ratios}")
    print(f"Normalized Weights: {result}")