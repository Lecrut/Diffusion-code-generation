class CredentialValidator:
    def __init__(self):
        self.username = 'admin'
        self.password = 'P@ssw0rd123'

    def validate_username(self, username):
        return username == self.username

    def validate_password(self, password):
        if len(password) < 12:
            return False
        if not any(char.isdigit() for char in password):
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char.islower() for char in password):
            return False
        if self.username.lower() in password.lower():
            return False
        return True

    def validate_credentials(self, username, password):
        return self.validate_username(username) and self.validate_password(password)

if __name__ == '__main__':
    validator = CredentialValidator()
    sample_username = 'admin'
    sample_password = 'P@ssw0rd123'
    result = validator.validate_credentials(sample_username, sample_password)
    print(f"Username: {sample_username}, Password: {sample_password}")
    print(f"Result: {result}")