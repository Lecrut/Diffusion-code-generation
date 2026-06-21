def can_vote(age):
    return age > 18

if __name__ == '__main__':
    test_ages = [17, 18, 19, 25]
    for age in test_ages:
        print(f"Age {age}: {can_vote(age)}")