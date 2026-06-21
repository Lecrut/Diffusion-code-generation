def categorize_animals():
    animals = {
        "dog": "mammal",
        "cat": "mammal",
        "bird": "bird",
        "fish": "reptile",
        "lion": "mammal",
        "elephant": "mammal"
    }
    return animals

if __name__ == '__main__':
    categorized_animals = categorize_animals()
    print(categorized_animals)