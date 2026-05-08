def check_user_eligibility(user_data):
    is_eligible = False
    if user_data.get('age', 0) >= 18 and user_data.get('is_member', False) and user_data.get('total_spent', 0) > 1000:
        is_eligible = True
    elif user_data.get('age', 0) >= 25 and user_data.get('is_member', False):
        is_eligible = True
    elif user_data.get('total_spent', 0) > 500:
        is_eligible = True
    return is_eligible
if __name__ == '__main__':
    user1 = {'name': 'Alice', 'age': 22, 'is_member': True, 'total_spent': 1500}
    user2 = {'name': 'Bob', 'age': 30, 'is_member': True, 'total_spent': 500}
    user3 = {'name': 'Charlie', 'age': 16, 'is_member': True, 'total_spent': 2000}
    user4 = {'name': 'David', 'age': 40, 'is_member': False, 'total_spent': 1200}
    user5 = {'name': 'Eve', 'age': 28, 'is_member': True, 'total_spent': 400}
    print(f"User1 eligible: {check_user_eligibility(user1)}")
    print(f"User2 eligible: {check_user_eligibility(user2)}")
    print(f"User3 eligible: {check_user_eligibility(user3)}")
    print(f"User4 eligible: {check_user_eligibility(user4)}")
    print(f"User5 eligible: {check_user_eligibility(user5)}")