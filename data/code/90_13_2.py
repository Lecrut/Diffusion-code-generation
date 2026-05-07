if __name__ == '__main__':
    age_input = "25"
    permission_input = "True"
    try:
        age = int(age_input)
    except ValueError:
        age = -1
    try:
        permission = permission_input.lower() == "true"
    except Exception:
        permission = False
    access_granted = (age >= 18) or permission
    if access_granted:
        print("Access Granted")
    else:
        print("Access Denied")