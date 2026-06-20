def are_logically_equivalent(str1: str, str2: str) -> bool:
    return str1.strip().lower() == str2.strip().lower()

if __name__ == '__main__':
    print(are_logically_equivalent(" Hello ", "hello"))
    print(are_logically_equivalent("Python", "python3"))
    print(are_logically_equivalent("  Test  ", "test "))