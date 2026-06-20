USER_DATA = {
    "age": 25,
    "email": "example@example.com",
    "is_subscribed": True,
    "balance": 100.0
}

MIN_AGE = 18
MAX_AGE = 65
VALID_EMAIL_DOMAINS = ["example.com", "test.com"]
MIN_BALANCE = 50.0

def validate_user_data(user_data):
    is_age_valid = MIN_AGE <= user_data["age"] <= MAX_AGE
    is_email_valid = any(user_data["email"].endswith(domain) for domain in VALID_EMAIL_DOMAINS)
    is_subscribed_valid = user_data["is_subscribed"]
    is_balance_valid = user_data["balance"] >= MIN_BALANCE
    
    return all([is_age_valid, is_email_valid, is_subscribed_valid, is_balance_valid])

if __name__ == '__main__':
    result = validate_user_data(USER_DATA)
    print(result)