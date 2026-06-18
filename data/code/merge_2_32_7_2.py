class DataSetAnalyzer:
    def calculate_cardinality(self, data):
        unique_elements = set(data)
        return len(unique_elements)
if __name__ == '__main__':
    analyzer = DataSetAnalyzer()
    sample_data_1 = [1, 2, 2, 3, 4, 4, 4, 5]
    sample_data_2 = ['apple', 'banana', 'apple', 'orange', 'banana']
    sample_data_3 = [100, 200, 300, 100, 200]
    cardinality_1 = analyzer.calculate_cardinality(sample_data_1)
    print(f"Cardinality of {sample_data_1}: {cardinality_1}")
    cardinality_2 = analyzer.calculate_cardinality(sample_data_2)
    print(f"Cardinality of {sample_data_2}: {cardinality_2}")
    cardinality_3 = analyzer.calculate_cardinality(sample_data_3)
    print(f"Cardinality of {sample_data_3}: {cardinality_3}")