def determine_voting_status(age, threshold=18):
    if age >= threshold:
        return True
    else:
        return False

if __name__ == '__main__':
    print(determine_voting_status(18))
    print(determine_voting_status(17))
    print(determine_voting_status(25))
    print(determine_voting_status(16, 21))