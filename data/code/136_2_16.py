class UserDataValidator:
    def __init__(self):
        self.user_data = {
            'age': 25,
            'email': 'example@example.com',
            'is_active': True
        }

    @staticmethod
    def is_age_valid(age):
        return age >= 18

    @staticmethod
    def is_email_valid(email):
        return '@' in email and '.' in email

    @staticmethod
    def is_user_active(is_active):
        return is_active

    def validate_user(self):
        validation_results = {
            'age': self.is_age_valid(self.user_data['age']),
            'email': self.is_email_valid(self.user_data['email']),
            'is_active': self.is_user_active(self.user_data['is_active'])
        }
        if all(validation_results.values()):
            return "User is valid"
        else:
            return "User is invalid"

if __name__ == '__main__':
    validator = UserDataValidator()
    result = validator.validate_user()
    print(result)