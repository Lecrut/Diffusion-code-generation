def check_voting_eligibility(ages):
    return ["Eligible" if age >= 18 else "Ineligible" for age in ages]

if __name__ == "__main__":
    sample_ages = [17, 18, 19, 16, 25, 100]
    results = check_voting_eligibility(sample_ages)
    print(results)