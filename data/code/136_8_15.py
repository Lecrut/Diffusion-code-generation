class CredentialValidator:
    def __init__(self, username='admin', password='Password123'):
        self.username = username
        self.password = password

    def is_valid_username(self):
        return len(self.username) >= 8 and not any(char.isdigit() for char in self.username)

    def is_valid_password(self):
        return (len(self.password) >= 12 
                and any(char.isdigit() for char in self.password)
                and any(char.isupper() for char in self.password)
                and any(char.islower() for char in self.password)
                and not self.username.lower() in self.password.lower())

    def validate_credentials(self):
        return self.is_valid_username() and self.is_valid_password()

if __name__ == '__main__':
    validator = CredentialValidator()
    print(f"Username: {validator.username}, Password: {validator.password}")
    print(f"Valid Username: {validator.is_valid_username()}")
    print(f"Valid Password: {validator.is_valid_password()}")
    print(f"Credentials Valid: {validator.validate_credentials()}")