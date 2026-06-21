CHECKLIST = set([
    "apple", "banana", "cherry", "date", "elderberry",
    "fig", "grape", "honeydew", "kiwi", "lemon"
])

def items_exist_in_checklist(items):
    return all(item in CHECKLIST for item in items)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "orange"]
    print(items_exist_in_checklist(sample_items))