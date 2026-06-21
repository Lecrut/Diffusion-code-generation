def check_items(checklist, items):
    checklist_set = set(checklist)
    return all(item in checklist_set for item in items)

if __name__ == '__main__':
    sample_checklist = [
        "apple", "banana", "cherry", "date", "elderberry",
        "fig", "grape", "honeydew", "kiwi", "lemon"
    ]
    sample_items = ["banana", "date", "fig"]
    
    result = check_items(sample_checklist, sample_items)
    print(result)