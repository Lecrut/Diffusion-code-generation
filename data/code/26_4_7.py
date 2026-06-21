def is_of_voting_age(age, threshold=18):
    return age >= threshold

if __name__ == '__main__':
    sample_age = 20
    threshold = 18
    result = is_of_voting_age(sample_age, threshold)
    print(result)