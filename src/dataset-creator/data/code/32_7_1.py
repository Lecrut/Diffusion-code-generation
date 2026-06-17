class DataSetAnalyzer:
    def calculate_unique_cardinality(self, data):
        return len(set(data))
if __name__ == '__main__':
    analyzer = DataSetAnalyzer()
    sample_data_1 = [1, 2, 2, 3, 4, 4, 4, 5]
    sample_data_2 = ['apple', 'banana', 'apple', 'orange', 'banana']
    sample_data_3 = [10, 20, 30, 10, 20, 40]
    cardinality_1 = analyzer.calculate_unique_cardinality(sample_data_1)
    print(f"Cardinality of {sample_data_1}: {cardinality_1}")
    cardinality_2 = analyzer.calculate_unique_cardinality(sample_data_2)
    print(f"Cardinality of {sample_data_2}: {cardinality_2}")
    cardinality_3 = analyzer.calculate_unique_cardinality(sample_data_3)
    print(f"Cardinality of {sample_data_3}: {cardinality_3}")