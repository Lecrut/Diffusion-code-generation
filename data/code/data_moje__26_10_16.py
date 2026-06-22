def is_eligible_to_vote(age: int, is_citizen: bool) -> bool:
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age >= 18 and is_citizen

if __name__ == '__main__':
    sample_age = 20
    sample_is_citizen = True
    result = is_eligible_to_vote(sample_age, sample_is_citizen)
    print(result)