class UserDataValidator:
    REQUIRED_KEYS = {'username', 'age', 'email'}
    MIN_AGE = 18

    @staticmethod
    def validate_user_data(user_data):
        if not all(key in user_data for key in UserDataValidator.REQUIRED_KEYS):
            return False, "Missing required keys"

        if user_data['age'] < UserDataValidator.MIN_AGE:
            return False, "Age must be at least 18"

        if '@' not in user_data['email']:
            return False, "Invalid email format"

        return True, "User data is valid"

if __name__ == '__main__':
    sample_user_data = {
        'username': 'john_doe',
        'age': 25,
        'email': 'john.doe@example.com'
    }

    result, message = UserDataValidator.validate_user_data(sample_user_data)
    print(f"Validation result: {result}")
    print(f"Message: {message}")