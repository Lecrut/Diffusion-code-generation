def get_favorite_animals():
    favorite_animals = set()
    while True:
        user_input = input("Enter a favorite animal name (or 'done'): ")
        if user_input == 'done':
            break
        if user_input:
            favorite_animals.add(user_input.strip().lower())
    return favorite_animals
if __name__ == '__main__':
    print("Starting the process with hard-coded sample values.")
    sample_inputs = ["dog", "cat", "bird", "dog", "fish", "cat", "done", "Dog"]
    unique_animals = set()
    for animal in sample_inputs:
        if animal.lower() != 'done':
            unique_animals.add(animal.lower())
    print("Unique favorite animals found:", unique_animals)