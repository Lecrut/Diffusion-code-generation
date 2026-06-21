from typing import Set

CHECKLIST_MEMBERS: Set[str] = {"member1", "member2", "member3"}

def is_id_in_checklist(member_id: str) -> bool:
    return member_id in CHECKLIST_MEMBERS

if __name__ == '__main__':
    sample_id = "member2"
    print(is_id_in_checklist(sample_id))