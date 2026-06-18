def evaluate_conditions(user_id: int) -> None:
    if user_id < 10:
        print("User is a child.")
    elif 10 <= user_id <= 65:
        print("User is an adult.")
    else:
        print("User is senior.")
if __name__ == '__main__':
    sample_user = 25
    evaluate_conditions(sample_user)