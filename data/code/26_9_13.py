def can_vote(age: int) -> bool:
    return age > 18

if __name__ == '__main__':
    test_ages = [17, 18, 19, 21]
    for age in test_ages:
        print(can_vote(age))