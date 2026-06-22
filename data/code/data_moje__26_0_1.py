def is_eligible_to_vote(age: int) -> bool:
    return age >= 18

if __name__ == '__main__':
    age = 20
    print(is_eligible_to_vote(age))