class ChecklistChecker:
    CHECKLIST = {'apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grape'}

    @staticmethod
    def check_items(items):
        return items.intersection(ChecklistChecker.CHECKLIST)

if __name__ == '__main__':
    sample_items = ['banana', 'kiwi', 'apple']
    result = ChecklistChecker.check_items(set(sample_items))
    print(result)