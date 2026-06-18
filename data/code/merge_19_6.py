def load_favorites(filename):
    favorites = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                favorites.append(line.strip())
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return None
    return favorites
if __name__ == '__main__':
    file_name = 'favorites.txt'
    try:
        with open(file_name, 'w') as f:
            f.write("Dog\n")
            f.write("Cat\n")
            f.write("Bird\n")
    except IOError:
        pass
    animal_list = load_favorites(file_name)
    if animal_list is not None:
        print(animal_list)