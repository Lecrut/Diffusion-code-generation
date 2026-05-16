def check_user_eligibility(user_data):
    is_eligible = False
    if user_data.get('age', 0) >= 18 and user_data.get('is_member', False) and user_data.get('total_spent', 0) > 1000:
        is_eligible = True
    return is_eligible
if __name__ == '__main__':
    sample_users = [
        {'name': 'Alice', 'age': 25, 'is_member': True, 'total_spent': 1500},
        {'name': 'Bob', 'age': 16, 'is_member': True, 'total_spent': 2000},
        {'name': 'Charlie', 'age': 30, 'is_member': False, 'total_spent': 5000},
        {'name': 'David', 'age': 40, 'is_member': True, 'total_spent': 500},
        {'name': 'Eve', 'age': 22, 'is_member': True, 'total_spent': 1001}
    ]
    print("--- Checking User Eligibility ---")
    for user in sample_users:
        result = check_user_eligibility(user)
        print(f"User: {user['name']}, Eligible: {result}")
    print("\n--- Testing Specific Cases ---")
    test_cases = [
        {'age': 20, 'is_member': True, 'total_spent': 1001},                  
        {'age': 17, 'is_member': True, 'total_spent': 1001},                              
        {'age': 20, 'is_member': False, 'total_spent': 1001},                                
        {'age': 20, 'is_member': True, 'total_spent': 1000}                                 
    ]
    for i, user in enumerate(test_cases):
        result = check_user_eligibility(user)
        print(f"Test Case {i+1}: Eligible: {result}")