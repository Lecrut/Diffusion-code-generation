def get_unique_sorted_favorites(animal_names):
    unique_favorites = set(animal_names)
    sorted_favorites = sorted(list(unique_favorites))
    return sorted_favorites
if __name__ == '__main__':
    sample_data = [
        "dog",
        "cat",
        "dog",
        "bird",
        "cat",
        "fish",
        "dog",
        "bird"
    ]
    result = get_unique_sorted_favorites(sample_data)
    print(result)