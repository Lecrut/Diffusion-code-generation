def check_conditions(condition_a, condition_b):
    return condition_a and condition_b

if __name__ == '__main__':
    try:
        result = check_conditions(True, False)
    except Exception as e:
        print(f"An error occurred: {e}")
    else:
        print(result)