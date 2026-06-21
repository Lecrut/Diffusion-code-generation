def is_id_in_checklist(checklist_ids: set, target_id: str) -> bool:
    return target_id in checklist_ids

if __name__ == '__main__':
    checklist_members = {'001', '002', '003'}
    sample_id = '002'
    print(is_id_in_checklist(checklist_members, sample_id))