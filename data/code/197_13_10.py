checklist = {
    "apple": True,
    "banana": False,
    "cherry": True,
    "date": True,
    "elderberry": False,
}

def check_items(items_to_check):
    items_set = set(items_to_check)
    return all(item in checklist for item in items_to_check)

if __name__ == '__main__':
    sample_items = ["apple", "banana", "cherry"]
    print(check_items(sample_items))