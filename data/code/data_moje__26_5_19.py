def check_voting_eligibility(ages):
    results = []
    for age in ages:
        if age >= 18:
            results.append("Eligible")
        else:
            results.append("Ineligible")
    return results

if __name__ == "__main__":
    sample_ages = [16, 18, 25, 17, 19]
    print(check_voting_eligibility(sample_ages))