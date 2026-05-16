class TruthEvaluator:
    def process_list(self, data):
        true_count = 0
        false_count = 0
        for item in data:
            if item == 'True':
                true_count += 1
            elif item == 'False':
                false_count += 1
        return {"True": true_count, "False": false_count}
if __name__ == '__main__':
    evaluator = TruthEvaluator()
    sample_data = ['True', 'False', 'True', 'True', 'False', 'True', 'False', 'False']
    result = evaluator.process_list(sample_data)
    print(result)