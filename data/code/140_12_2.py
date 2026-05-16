class InputAnalyzer:
    def analyze(self, data):
        true_count = 0
        false_count = 0
        for condition in data:
            if condition:
                true_count += 1
            else:
                false_count += 1
        return {
            "true_count": true_count,
            "false_count": false_count
        }
if __name__ == '__main__':
    analyzer = InputAnalyzer()
    sample_data = [True, False, True, True, False, True, False]
    results = analyzer.analyze(sample_data)
    print(results)