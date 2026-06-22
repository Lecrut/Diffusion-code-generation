def check_conditions(str1: str, str2: str, num1: int, num2: int) -> str:
    if str1 == str2 and num1 != num2:
        return "Conditions met"
    return "Conditions not met"

if __name__ == '__main__':
    result = check_conditions("hello", "hello", 10, 20)
    print(result)