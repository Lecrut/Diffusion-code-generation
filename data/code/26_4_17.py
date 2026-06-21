def check_voting_status(age, threshold=18):
    if age >= threshold:
        return True
    return False

if __name__ == '__main__':
    print(check_voting_status(20))
    print(check_voting_status(16))
    print(check_voting_status(18))
    print(check_voting_status(17, threshold=21))