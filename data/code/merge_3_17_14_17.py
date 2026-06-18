def get_user_choice(user: int) -> str:
    """Prints a message indicating if user is even or odd."""
    
    result = "even" if user % 2 == 0 else "odd"
    print(f"You entered {user} which was an number that was determined to be '{result}' in this session.")

if __name__ == '__main__':
    sample_values = [1, 56893]
    
    for value_in_session in range(0, len(sample_values)):
        user_value_for_current_session = sample_values[value_in_session]
        
        get_user_choice(user_value_for_current_session)