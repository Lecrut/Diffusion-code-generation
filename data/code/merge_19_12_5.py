class AnimalFavorites:
    def __init__(self):
        self.favorites = []
    def add_favorite(self, animal):
        self.favorites.append(animal)
    def display_favorites(self):
        for animal in self.favorites:
            print(animal)
if __name__ == '__main__':
    favorites_manager = AnimalFavorites()
    sample_animals = ["Lion", "Tiger", "Elephant", "Bear"]
    for animal in sample_animals:
        favorites_manager.add_favorite(animal)
        print(f"Added favorite: {animal}")
    print("\n--- Displaying Favorites ---")
    favorites_manager.display_favorites()