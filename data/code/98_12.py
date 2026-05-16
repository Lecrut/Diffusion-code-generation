def check_access(age, access_level, subscription_status):
    if age >= 18 and access_level == "premium" and subscription_status == True:
        return True
    else:
        return False
if __name__ == '__main__':
    user_age = 25
    user_access_level = "premium"
    user_subscription = True
    can_proceed = check_access(user_age, user_access_level, user_subscription)
    if can_proceed:
        print("Access granted. Proceeding with the operation.")
    else:
        print("Access denied. One or more conditions were not met.")