def evaluate_conditions(user_input: str) -> None:
    if user_input == "hello":
        print("Greeting detected.")
    elif len(user_input) > 5:
        print("Input is long enough.")
    else:
        print("No specific condition met.")
if __name__ == '__main__':
    sample_value = "world"
    evaluate_conditions(sample_value)