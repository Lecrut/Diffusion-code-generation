def is_eligible_to_vote(age):
    return age >= 18

if __name__ == '__main__':
    sample_ages = [17, 18, 25, 30]
    for age in sample_ages:
        print(is_eligible_to_vote(age))