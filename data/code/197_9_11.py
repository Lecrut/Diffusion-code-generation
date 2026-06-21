def is_member(checklist: dict, member_id: int) -> bool:
    return member_id in checklist

if __name__ == '__main__':
    members = {10, 5, 10, 15, 20}
    sample_ids = [10, 99]
    results = {member_id: is_member(members, member_id) for member_id in sample_ids}
    print(results)