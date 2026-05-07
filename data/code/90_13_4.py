if __name__ == '__main__':
    age_input = "25"
    permission_input = "True"
    try:
        age = int(age_input)
    except ValueError:
        age = -1
    permission = permission_input.lower() == "true"
    if age >= 18 or permission:
        print("Access Granted")
    else:
        print("Access Denied")