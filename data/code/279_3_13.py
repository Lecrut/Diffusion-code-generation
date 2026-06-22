SAMPLE_PEOPLE = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

def print_person_details(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    print_person_details(SAMPLE_PEOPLE)