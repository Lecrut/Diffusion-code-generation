if __name__ == '__main__':
    age_input = "25"
    permission_input = "True"
    try:
        age = int(age_input)
        permission = permission_input.lower() == "true"
    except ValueError:
        print("Invalid age input.")
        exit()
    if age >= 18 or permission:
        print("Access Granted")
    else:
        print("Access Denied")