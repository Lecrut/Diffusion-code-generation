from typing import Set

CHECKLIST_MEMBERS: Set[str] = {"12345", "67890", "54321"}

def is_id_in_checklist(check_id: str) -> bool:
    return check_id in CHECKLIST_MEMBERS

if __name__ == '__main__':
    sample_id = "12345"
    print(is_id_in_checklist(sample_id))