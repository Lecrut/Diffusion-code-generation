class AnimalFavorites:
    def __init__(self):
        self._favorites = set()
    def add_favorite(self, animal_name):
        self._favorites.add(animal_name)
    def get_favorite(self, animal_name):
        return animal_name in self._favorites
    def list_favorites(self):
        return list(self._favorites)
if __name__ == '__main__':
    favorites = AnimalFavorites()
    favorites.add_favorite("Lion")
    favorites.add_favorite("Elephant")
    favorites.add_favorite("Tiger")
    favorites.add_favorite("Lion")
    print(favorites.list_favorites())
    print(f"Is Elephant a favorite? {favorites.get_favorite('Elephant')}")
    print(f"Is Bear a favorite? {favorites.get_favorite('Bear')}")