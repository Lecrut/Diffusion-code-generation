def get_voting_status(age, threshold=18):
    return "eligible" if age >= threshold else "ineligible"

if __name__ == '__main__':
    print(get_voting_status(20))
    print(get_voting_status(15))
    print(get_voting_status(18))
    print(get_voting_status(17, 21))