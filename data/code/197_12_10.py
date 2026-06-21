class ChecklistValidator:
    def __init__(self, checklist):
        self.checklist_set = frozenset(checklist)

    def validate_items(self, items):
        return all(item in self.checklist_set for item in items)

if __name__ == '__main__':
    validator = ChecklistValidator(['apple', 'banana', 'cherry'])
    result_1 = validator.validate_items(['banana', 'grape'])
    print("Result 1:", result_1)