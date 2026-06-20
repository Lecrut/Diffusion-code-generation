import operator
MIN_AGE = 18
MAX_AGE = 65
VALID_GENDERS = {'Male', 'Female'}

def validate_user_data(user_data):
    age = user_data.get('age')
    gender = user_data.get('gender')
    if (age is not None and MIN_AGE <= age <= MAX_AGE) and (gender is not None and gender in VALID_GENDERS):
        return True
    return False
if __name__ == '__main__':
    sample_user_data = {'age': 25, 'gender': 'Male'}
    result = validate_user_data(sample_user_data)
    print(result)