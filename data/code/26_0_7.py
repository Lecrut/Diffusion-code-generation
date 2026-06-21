def is_eligible_to_vote(age: int) -> bool:
    return age >= 18

if __name__ == '__main__':
    sample_age = 20
    result = is_eligible_to_vote(sample_age)
    print(result)