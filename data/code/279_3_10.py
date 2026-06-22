PEOPLE = {
    "Alice": 30,
    "Bob": 25,
    "Charlie": 35
}

def print_ages(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    print_ages(PEOPLE)