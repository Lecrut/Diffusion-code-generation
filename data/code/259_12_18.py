class ValueExtremes:
    def find_min(self, values):
        return min(values) if values else None

    def find_max(self, values):
        return max(values) if values else None

if __name__ == '__main__':
    extremes = ValueExtremes()
    sample_values = [12, 7, 25, 3, 48]
    min_value = extremes.find_min(sample_values)
    max_value = extremes.find_max(sample_values)
    print(f"Sample values: {sample_values}")
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")