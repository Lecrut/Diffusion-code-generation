from typing import Dict

def map_checklist_items(checklist: Dict[str, bool]) -> Dict[str, str]:
    status_mapping = {
        True: "Member",
        False: "Non-Member"
    }
    return {item: status_mapping[status] for item, status in checklist.items()}

if __name__ == '__main__':
    sample_checklist = {
        "Item1": True,
        "Item2": False,
        "Item3": True
    }
    print(map_checklist_items(sample_checklist))