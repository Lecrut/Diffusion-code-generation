def check_age_eligibility(citizen_details):
    return 'age' in citizen_details and citizen_details['age'] >= 18

if __name__ == '__main__':
    sample_data_1 = {'name': 'Alice', 'age': 25}
    sample_data_2 = {'name': 'Bob', 'age': 17}
    sample_data_3 = {'name': 'Charlie'}
    print(check_age_eligibility(sample_data_1))
    print(check_age_eligibility(sample_data_2))
    print(check_age_eligibility(sample_data_3))