from typing import Set

CHECKLIST_MEMBERS: Set[str] = {"member1", "member2", "member3"}

def is_member(checklist_id: str) -> bool:
    return checklist_id in CHECKLIST_MEMBERS

if __name__ == '__main__':
    sample_id = "member2"
    print(is_member(sample_id))