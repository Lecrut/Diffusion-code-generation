def get_voting_status(age, threshold=18):
    is_voter = age >= threshold
    return is_voter

if __name__ == '__main__':
    ages = [16, 18, 21]
    for age in ages:
        print(get_voting_status(age))