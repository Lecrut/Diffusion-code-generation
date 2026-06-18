try:
    with open('favorites.txt', 'r') as file:
        favorite_animals = file.readlines()
except FileNotFoundError:
    favorite_animals = []
favorite_list = [line.strip() for line in favorite_animals if line.strip()]
if __name__ == '__main__':
    print(favorite_list)