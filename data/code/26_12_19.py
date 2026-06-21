def check_voting_eligibility(age: int, has_criminal_record: bool, is_citizen: bool) -> str:
    if age < 18:
        return "Not eligible: Underage"
    if not is_citizen:
        return "Not eligible: Not a citizen"
    if has_criminal_record:
        return "Not eligible: Criminal record"
    return "Eligible to vote"

if __name__ == '__main__':
    age = 25
    has_criminal_record = False
    is_citizen = True
    result = check_voting_eligibility(age, has_criminal_record, is_citizen)
    print(result)

    age2 = 16
    has_criminal_record2 = False
    is_citizen2 = True
    result2 = check_voting_eligibility(age2, has_criminal_record2, is_citizen2)
    print(result2)

    age3 = 30
    has_criminal_record3 = True
    is_citizen3 = True
    result3 = check_voting_eligibility(age3, has_criminal_record3, is_citizen3)
    print(result3)

    age4 = 40
    has_criminal_record4 = False
    is_citizen4 = False
    result4 = check_voting_eligibility(age4, has_criminal_record4, is_citizen4)
    print(result4)