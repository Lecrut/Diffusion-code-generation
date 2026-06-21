def manage_fruit_list():
    fruits = ['apple', 'banana', 'orange']

    def append_fruit(fruit):
        if fruit not in fruits:
            fruits.append(fruit)
            return True
        return False

    def remove_fruit(fruit):
        if fruit in fruits:
            fruits.remove(fruit)
            return True
        return False
    return (fruits, append_fruit, remove_fruit)
if __name__ == '__main__':
    fruits, append_fruit, remove_fruit = manage_fruit_list()
    print('Initial fruits:', fruits)
    if append_fruit('grape'):
        print("Fruits after appending 'grape':", fruits)
    else:
        print("'grape' already exists in the list.")
    if remove_fruit('banana'):
        print("Fruits after removing 'banana':", fruits)
    else:
        print("'banana' not found in the list.")