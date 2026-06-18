def get_user_input(prompt_text):
    """Simulates a prompt by returning hard-coded values since input() is forbidden."""
    return float(10), 5

if __name__ == '__main__':
    num1, num2 = get_user_input("Please enter two numbers to compare.")
    
    if num1 > num2:
        print(f"{num1} is greater than {num2}")
    else:
        print(f"{num1} is not greater than {num2}")