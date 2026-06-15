class AnimalFavorites:
    def __init__(self):
        self.favorites = []
    def add_favorite(self, animal):
        self.favorites.append(animal)
    def display_favorites(self):
        if self.favorites:
            print("Favorite Animals:")
            for animal in self.favorites:
                print(f"- {animal}")
        else:
            print("No favorite animals added yet.")
if __name__ == '__main__':
    favorites_manager = AnimalFavorites()
    sample_animals = ["Lion", "Tiger", "Elephant", "Bear", "Wolf"]
    for animal in sample_animals:
        favorites_manager.add_favorite(animal)
    favorites_manager.display_favorites()