def print_individual_ages(people):
    for name, age in people.items():
        print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Eve": 28,
        "Frank": 40,
        "Grace": 32
    }
    print_individual_ages(sample_people)