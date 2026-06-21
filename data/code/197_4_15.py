from typing import Dict

def map_checklist_items(checklist: Dict[str, bool]) -> Dict[str, str]:
    status_map = {
        True: "Active",
        False: "Inactive"
    }
    return {item: status_map[status] for item, status in checklist.items()}

if __name__ == '__main__':
    sample_checklist = {
        "Item 1": True,
        "Item 2": False,
        "Item 3": True
    }
    print(map_checklist_items(sample_checklist))