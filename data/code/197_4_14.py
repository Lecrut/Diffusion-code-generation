from typing import Dict

def map_checklist_items(checklist: dict) -> Dict[str, str]:
    membership_status = {
        'item1': 'Member',
        'item2': 'Non-Member',
        'item3': 'Pending'
    }
    if not isinstance(checklist, dict):
        raise ValueError("Input must be a dictionary")
    
    return {item: membership_status.get(item, 'Unknown') for item in checklist}

if __name__ == '__main__':
    sample_checklist = {'item1': True, 'item4': False}
    try:
        result = map_checklist_items(sample_checklist)
        print(result)
    except ValueError as e:
        print(e)