def determine_voting_status(age, voting_age_threshold=18):
    if age >= voting_age_threshold:
        return "eligible"
    return "ineligible"

if __name__ == "__main__":
    sample_age = 20
    result = determine_voting_status(sample_age)
    print(result)
    sample_age_young = 16
    result_young = determine_voting_status(sample_age_young)
    print(result_young)
    result_custom = determine_voting_status(17, 17)
    print(result_custom)