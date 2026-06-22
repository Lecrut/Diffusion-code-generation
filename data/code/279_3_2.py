def print_person_details(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    print_person_details(sample_people)