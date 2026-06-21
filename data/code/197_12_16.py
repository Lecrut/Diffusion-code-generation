class ChecklistValidator:
    def __init__(self, checklist):
        self.checklist_set = frozenset(checklist)

    def validate_items(self, items):
        return all(item in self.checklist_set for item in items)

if __name__ == '__main__':
    validator = ChecklistValidator(['apple', 'banana', 'cherry'])
    items_to_check_1 = ['banana', 'grape']
    result_1 = validator.validate_items(items_to_check_1)
    print("Result 1:", result_1)

    items_to_check_2 = ['apple', 'cherry']
    result_2 = validator.validate_items(items_to_check_2)
    print("Result 2:", result_2)