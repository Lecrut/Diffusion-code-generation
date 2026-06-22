class ValueExtremes:
    def find_min(self, data_list):
        if not data_list:
            return None
        return min(data_list)
    
    def find_max(self, data_list):
        if not data_list:
            return None
        return max(data_list)

if __name__ == '__main__':
    extremes = ValueExtremes()
    sample_values = [10, 5, 20, 8, 15]
    print(f"Minimum value: {extremes.find_min(sample_values)}")
    print(f"Maximum value: {extremes.find_max(sample_values)}")