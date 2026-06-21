def check_voting_status(age, threshold=18):
    return age >= threshold

if __name__ == '__main__':
    print(check_voting_status(16))
    print(check_voting_status(18))
    print(check_voting_status(21))
    print(check_voting_status(18, threshold=21))