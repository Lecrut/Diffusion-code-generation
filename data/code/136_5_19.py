class LogicalOperatorEvaluator:
    def __init__(self):
        self.set_a = {"apple", "banana", "cherry"}
        self.set_b = {"banana", "date", "elderberry"}

    def evaluate_expression(self, item):
        condition_a = item in self.set_a
        condition_b = item not in self.set_b
        result = condition_a and condition_b
        return result

if __name__ == '__main__':
    evaluator = LogicalOperatorEvaluator()
    item_to_check = "apple"
    result1 = evaluator.evaluate_expression(item_to_check)
    print(f"Checking '{item_to_check}': In set A ({evaluator.set_a}) AND Not in set B ({evaluator.set_b}) -> {result1}")
    
    item_to_check_2 = "banana"
    result2 = evaluator.evaluate_expression(item_to_check_2)
    print(f"Checking '{item_to_check_2}': In set A ({evaluator.set_a}) AND Not in set B ({evaluator.set_b}) -> {result2}")
    
    item_to_check_3 = "grape"
    result3 = evaluator.evaluate_expression(item_to_check_3)
    print(f"Checking '{item_to_check_3}': In set A ({evaluator.set_a}) AND Not in set B ({evaluator.set_b}) -> {result3}")