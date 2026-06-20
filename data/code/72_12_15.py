class ElementComparer:
    def find_inequality(self, data):
        if not isinstance(data, list):
            raise TypeError("Input 'data' must be a list.")
        
        inequalities = []
        for i in range(len(data) - 1):
            if data[i] != data[i + 1]:
                inequalities.append((i, data[i], data[i + 1]))
        
        return inequalities

if __name__ == '__main__':
    comparer = ElementComparer()
    sample_data = [1, "apple", [2, 3], {"a": 4}, 5.5]
    print("--- Inequalities Found ---")
    for index, value1, value2 in comparer.find_inequality(sample_data):
        print(f"Index: {index}, Value1: {value1}, Value2: {value2}")