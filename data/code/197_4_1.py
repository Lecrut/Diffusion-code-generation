def map_checklist_items(checklist: dict) -> dict:
    membership_status = {
        'item1': 'Member',
        'item2': 'Non-Member',
        'item3': 'Pending'
    }
    return {item: membership_status.get(item, 'Unknown') for item in checklist}

if __name__ == '__main__':
    sample_checklist = {'item1', 'item4'}
    result = map_checklist_items(sample_checklist)
    print(result)