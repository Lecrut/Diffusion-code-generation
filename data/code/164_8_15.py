def categorize_animals(animals):
    endothermic = {"dog", "cat", "bird", "lion", "cow"}
    ectothermic = {"fish", "snake"}

    categorized_animals = {
        "endothermic": {},
        "ectothermic": {}
    }

    for animal in animals:
        if animal.strip() in endothermic:
            categorized_animals["endothermic"][animal.strip()] = "Endothermic"
        elif animal.strip() in ectothermic:
            categorized_animals["ectothermic"][animal.strip()] = "Ectothermic"

    return categorized_animals

if __name__ == '__main__':
    sample_animals = ["dog", "cat", "bird", "fish", "lion", "cow", "snake"]
    organized_data = categorize_animals(sample_animals)
    print(organized_data)