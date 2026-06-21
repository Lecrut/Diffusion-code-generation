class NameAnalyzer:
    def calculate_average_length(self, names_list):
        if not names_list:
            return 0
        total_length = sum(len(name) for name in names_list)
        average_length = total_length / len(names_list)
        return average_length

    def find_names_longer_than_average(self, names_list):
        average_length = self.calculate_average_length(names_list)
        longer_names = [name for name in names_list if len(name) > average_length]
        return longer_names

if __name__ == '__main__':
    analyzer = NameAnalyzer()
    sample_names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    print("Names:", sample_names)
    longer_than_average = analyzer.find_names_longer_than_average(sample_names)
    print("Names longer than average length:", longer_than_average)