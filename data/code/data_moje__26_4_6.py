def get_voting_status(age, threshold=18):
    if age >= threshold:
        return "eligible"
    return "ineligible"

if __name__ == '__main__':
    print(get_voting_status(20))
    print(get_voting_status(17))
    print(get_voting_status(18))