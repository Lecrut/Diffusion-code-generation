def check_access(age, access_level, subscription_status):
    if age >= 18 and access_level == "premium" and subscription_status == True:
        return True
    else:
        return False
if __name__ == '__main__':
    user_age = 25
    access_level = "premium"
    subscription_status = True
    result = check_access(user_age, access_level, subscription_status)
    if result:
        print("Access Granted: User meets all requirements.")
    else:
        print("Access Denied: One or more conditions were not met.")