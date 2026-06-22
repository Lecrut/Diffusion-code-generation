def print_names_and_ages(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    print_names_and_ages(sample_people)