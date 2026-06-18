names = {"Alice", "Bob", "Charlie"}
def check_name_existence(name):
    return name in names
if __name__ == '__main__':
    test_cases = ["Alice", "David", "Eve"]
    for person in test_cases:
        result = check_name_existence(person)
        print(f"{person}: {result}")