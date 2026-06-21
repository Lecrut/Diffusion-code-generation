class ChecklistChecker:
    CHECKLIST = {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

    @staticmethod
    def check_items(items):
        return items.intersection(ChecklistChecker.CHECKLIST)

if __name__ == '__main__':
    sample_items = {'banana', 'date', 'kiwi'}
    result = ChecklistChecker.check_items(sample_items)
    print("Checked Items:", result)