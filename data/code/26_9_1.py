VOTING_RULES = {"age": 18}

def can_vote(age):
    threshold = VOTING_RULES["age"]
    return age > threshold

if __name__ == '__main__':
    results = []
    for age in [17, 18, 19]:
        results.append(can_vote(age))
    print(results)