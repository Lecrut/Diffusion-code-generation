def check_voting_status(age, threshold=18):
    return age >= threshold

if __name__ == '__main__':
    result = check_voting_status(20)
    print(result)