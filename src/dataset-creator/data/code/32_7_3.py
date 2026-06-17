class LargeDataSetHandler:
    def calculate_cardinality(self, data):
        return len(set(data))
if __name__ == '__main__':
    handler = LargeDataSetHandler()
    sample_data_1 = [1, 2, 3, 4, 1, 2, 5, 3]
    sample_data_2 = ['apple', 'banana', 'apple', 'orange', 'banana']
    sample_data_3 = [100, 100, 100, 100]
    sample_data_4 = []
    print(f"Cardinality of sample_data_1: {handler.calculate_cardinality(sample_data_1)}")
    print(f"Cardinality of sample_data_2: {handler.calculate_cardinality(sample_data_2)}")
    print(f"Cardinality of sample_data_3: {handler.calculate_cardinality(sample_data_3)}")
    print(f"Cardinality of sample_data_4: {handler.calculate_cardinality(sample_data_4)}")