class ChecklistManager:
    def __init__(self, items):
        self.items = set(items)

    def is_member(self, item):
        return item in self.items

if __name__ == '__main__':
    sample_checklist = ChecklistManager([10, 20, 30, 40, 50])
    item_to_check = 30
    result = sample_checklist.is_member(item_to_check)
    print(f"Checklist: {sample_checklist.items}")
    print(f"Checking for item: {item_to_check}")
    print(f"Is {item_to_check} in the checklist? {result}")

    sample_checklist_2 = ChecklistManager(['apple', 'banana', 'cherry'])
    item_to_check_2 = 'apple'
    result_2 = sample_checklist_2.is_member(item_to_check_2)
    print(f"\nChecklist: {sample_checklist_2.items}")
    print(f"Checking for item: {item_to_check_2}")
    print(f"Is {item_to_check_2} in the checklist? {result_2}")