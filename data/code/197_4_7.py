def validate_checklist(checklist: dict) -> bool:
    expected_keys = {'item1', 'item2', 'item3'}
    if not expected_keys.issubset(checklist):
        return False
    return True

def map_checklist_items(checklist: dict) -> dict:
    membership_status = {
        'item1': 'Member',
        'item2': 'Non-Member',
        'item3': 'Pending'
    }
    if not validate_checklist(checklist):
        raise ValueError("Invalid checklist items")
    return {item: membership_status.get(item, 'Unknown') for item in checklist}

if __name__ == '__main__':
    sample_checklist = {'item1', 'item2'}
    result = map_checklist_items(sample_checklist)
    print(result)