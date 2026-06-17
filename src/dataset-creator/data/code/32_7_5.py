class DataSetAnalyzer:
    def calculate_unique_cardinality(self, data):
        unique_elements = set(data)
        return len(unique_elements)
if __name__ == '__main__':
    analyzer = DataSetAnalyzer()
    sample_data1 = [1, 2, 3, 4, 1, 2, 5, 3]
    sample_data2 = ['apple', 'banana', 'apple', 'orange', 'banana']
    sample_data3 = [10, 20, 30, 10, 40, 50, 10]
    cardinality1 = analyzer.calculate_unique_cardinality(sample_data1)
    print(f"Cardinality of {sample_data1}: {cardinality1}")
    cardinality2 = analyzer.calculate_unique_cardinality(sample_data2)
    print(f"Cardinality of {sample_data2}: {cardinality2}")
    cardinality3 = analyzer.calculate_unique_cardinality(sample_data3)
    print(f"Cardinality of {sample_data3}: {cardinality3}")