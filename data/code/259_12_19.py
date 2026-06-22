class ValueExtremes:
    def find_min(self, numbers):
        if not numbers:
            return None
        return min(numbers)
    
    def find_max(self, numbers):
        if not numbers:
            return None
        return max(numbers)

if __name__ == '__main__':
    extremes = ValueExtremes()
    sample_values = [10, 5, 20, 8, 15]
    min_val = extremes.find_min(sample_values)
    max_val = extremes.find_max(sample_values)
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")