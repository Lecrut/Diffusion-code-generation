def check_user_eligibility(user_data):
    is_eligible = False
    if user_data.get('age', 0) >= 18 and user_data.get('is_member', False) and user_data.get('total_spent', 0) > 1000:
        is_eligible = True
    elif user_data.get('age', 0) >= 25 and user_data.get('total_spent', 0) > 500:
        is_eligible = True
    return is_eligible
if __name__ == '__main__':
    user1 = {'name': 'Alice', 'age': 22, 'is_member': True, 'total_spent': 1500}
    user2 = {'name': 'Bob', 'age': 30, 'is_member': True, 'total_spent': 800}
    user3 = {'name': 'Charlie', 'age': 45, 'is_member': False, 'total_spent': 2000}
    user4 = {'name': 'David', 'age': 28, 'is_member': True, 'total_spent': 600}
    print(f"User 1 eligible: {check_user_eligibility(user1)}")
    print(f"User 2 eligible: {check_user_eligibility(user2)}")
    print(f"User 3 eligible: {check_user_eligibility(user3)}")
    print(f"User 4 eligible: {check_user_eligibility(user4)}")