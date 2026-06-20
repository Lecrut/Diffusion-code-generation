def check_or_condition(age: int, permission: bool) -> bool:
    return age >= 18 or permission

if __name__ == '__main__':
    result = check_or_condition(25, True)
    print(result)