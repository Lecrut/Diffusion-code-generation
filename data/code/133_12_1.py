class TruthEvaluator:
    def process_list(self, data):
        true_count = 0
        false_count = 0
        for item in data:
            if item.lower() == 'true':
                true_count += 1
            elif item.lower() == 'false':
                false_count += 1
        return {"true": true_count, "false": false_count}
if __name__ == '__main__':
    evaluator = TruthEvaluator()
    sample_data = ["True", "false", "true", "false", "true", "false", "TRUE"]
    result = evaluator.process_list(sample_data)
    print(result)