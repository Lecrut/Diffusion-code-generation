def map_checklist_items(checklist: dict) -> dict:
    membership_status = {
        'item1': 'active',
        'item2': 'inactive',
        'item3': 'pending'
    }
    return {item: status for item, status in checklist.items() if item in membership_status}

if __name__ == '__main__':
    sample_checklist = {'item1': True, 'item4': False}
    print(map_checklist_items(sample_checklist))