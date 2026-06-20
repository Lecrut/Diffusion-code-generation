user_data = {
    'age': 25,
    'access_level': 'admin',
    'subscription_status': True
}

required_conditions = {
    'min_age': lambda age: age >= 18,
    'high_access': lambda level: level in ['admin', 'manager'],
    'active_subscription': lambda status: status is True
}

def check_conditions(data, conditions):
    result = True
    for condition_name, condition_func in conditions.items():
        if not condition_func(data.get(condition_name)):
            result = False
            break
    return result

if __name__ == '__main__':
    result = check_conditions(user_data, required_conditions)
    print(result)