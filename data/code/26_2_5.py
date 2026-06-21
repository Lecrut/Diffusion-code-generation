def is_adult(citizen_details):
    return isinstance(citizen_details, dict) and 'age' in citizen_details and citizen_details['age'] >= 18

if __name__ == '__main__':
    sample_adult = {"name": "Alice", "age": 20}
    sample_minor = {"name": "Bob", "age": 15}
    sample_no_age = {"name": "Charlie"}
    
    result_adult = is_adult(sample_adult)
    result_minor = is_adult(sample_minor)
    result_no_age = is_adult(sample_no_age)
    
    print(result_adult)
    print(result_minor)
    print(result_no_age)