if __name__ == '__main__':
    age_input = 25
    permission_input = True
    if isinstance(age_input, int) and isinstance(permission_input, bool):
        if age_input >= 18 or permission_input:
            print("Access Granted")
        else:
            print("Access Denied")
    else:
        print("Invalid input types provided")