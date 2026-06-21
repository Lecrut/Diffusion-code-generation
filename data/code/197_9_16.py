from typing import Set

CHECKLIST_MEMBERS: Set[str] = {"member1", "member2", "member3"}

def is_id_in_checklist(id: str) -> bool:
    return id in CHECKLIST_MEMBERS

if __name__ == '__main__':
    sample_id = "member2"
    print(is_id_in_checklist(sample_id))