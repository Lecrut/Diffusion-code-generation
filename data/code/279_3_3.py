def print_ages(people):
    if not isinstance(people, dict):
        raise ValueError("Input must be a dictionary")
    
    for name, age in people.items():
        if not isinstance(name, str) or not isinstance(age, int):
            raise ValueError("Dictionary keys must be strings and values must be integers")
        
        print(f"{name}: {age}")

if __name__ == '__main__':
    sample_people = {
        "Alice": 30,
        "Bob": 25,
        "Charlie": 35
    }
    
    try:
        print_ages(sample_people)
    except ValueError as e:
        print(e)