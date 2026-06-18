def process_animal_names(sample_inputs):
    favorite_animals = set()
    input_stream = iter(sample_inputs)
    while True:
        try:
            animal = next(input_stream)
            if animal.lower() == 'done':
                break
            favorite_animals.add(animal.strip())
        except StopIteration:
            break
    return favorite_animals
if __name__ == '__main__':
    sample_data = [
        "Dog",
        "Cat",
        "Bird",
        "Dog",
        "Fish",
        "cat",
        "Done",
        "Bird",
        "Rabbit"
    ]
    result = process_animal_names(sample_data)
    print(result)