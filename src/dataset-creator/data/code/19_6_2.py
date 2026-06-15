try:
    with open('favorites.txt', 'r') as file:
        favorite_animals = file.readlines()
except FileNotFoundError:
    favorite_animals = []
if __name__ == '__main__':
    print(favorite_animals)