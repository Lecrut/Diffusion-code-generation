def print_individual_ages(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Eve": 28,
        "Frank": 32,
        "Grace": 29
    }
    print_individual_ages(sample_people)