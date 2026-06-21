class ChecklistValidator:

    def __init__(self, checklist):
        self.checklist_set = frozenset(checklist)

    def is_item_in_checklist(self, item):
        return item in self.checklist_set
if __name__ == '__main__':
    validator = ChecklistValidator(['apple', 'banana', 'cherry'])
    print(validator.is_item_in_checklist('banana'))
    print(validator.is_item_in_checklist('grape'))